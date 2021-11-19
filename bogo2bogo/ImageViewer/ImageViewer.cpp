#include "ImageViewer.h"
#include "ui_ImageViewer.h"
#include <QtCore>
#include <QtGui>
#include <QtWidgets>

ImageViewer::ImageViewer(QWidget *parent) : QMainWindow(parent), image(nullptr)
{
  setWindowTitle("ImageViewer");
  scaleFactor = 1.0;
  imageLoaded = false;
  imageLabel = new QLabel("");
  scrollArea = new QScrollArea();

  imageLabel->setBackgroundRole(QPalette::Base);
  imageLabel->setSizePolicy(QSizePolicy::Ignored, QSizePolicy::Ignored);
  imageLabel->setScaledContents(true);

  scrollArea->setBackgroundRole(QPalette::Dark);
  scrollArea->setWidget(imageLabel);
  scrollArea->setVisible(false);
  setCentralWidget(scrollArea);

  createActions();
  createMenus();
  createToolbar();
  statusBar()->showMessage("");

  // set initial size to 3/5 of screen
  resize(QGuiApplication::primaryScreen()->availableSize() * 3 / 5);
  setWindowIcon(QIcon(":/ImageViewer-icon.png")); // load an image
}

ImageViewer::~ImageViewer() {}

void ImageViewer::createActions()
{
  openAction = new QAction("&Open...", this);
  openAction->setShortcut(QKeySequence::Open);
  openAction->setIcon(QIcon(":/open.png"));
  openAction->setStatusTip("Open a new image file to view");
  QObject::connect(openAction, SIGNAL(triggered()), this, SLOT(open()));

  printAction = new QAction("&Print...", this);
  printAction->setShortcut(QKeySequence::Print);
  printAction->setIcon(QIcon(":/print.png"));
  printAction->setStatusTip("Print the current image");
  QObject::connect(printAction, SIGNAL(triggered()), this, SLOT(print()));
  printAction->setEnabled(false);

  exitAction = new QAction("E&xit", this);
  exitAction->setShortcut(QKeySequence("Ctrl+Q"));
  exitAction->setStatusTip("Quit the application");
  QObject::connect(exitAction, SIGNAL(triggered()), QApplication::instance(), SLOT(quit()));

  zoomInAction = new QAction("Zoom &in (25%)", this);
  zoomInAction->setShortcut(QKeySequence("Ctrl++"));
  zoomInAction->setIcon(QIcon(":/zoom_in.png"));
  zoomInAction->setStatusTip("Zoom into the image by 25%");
  QObject::connect(zoomInAction, SIGNAL(triggered()), this, SLOT(zoomIn()));
  zoomInAction->setEnabled(false);

  zoomOutAction = new QAction("Zoom &out (25%)", this);
  zoomOutAction->setShortcut(QKeySequence("Ctrl+-"));
  zoomOutAction->setIcon(QIcon(":/zoom_out.png"));
  zoomOutAction->setStatusTip("Zoom out of the image by 25%");
  QObject::connect(zoomOutAction, SIGNAL(triggered()), this, SLOT(zoomOut()));
  zoomOutAction->setEnabled(false);

  zoomNormalAction = new QAction("&Normal size", this);
  zoomNormalAction->setShortcut(QKeySequence("Ctrl+0"));
  zoomNormalAction->setStatusTip("Zoom to normal size (reset zoom)");
  QObject::connect(zoomNormalAction, SIGNAL(triggered()), this, SLOT(normalSize()));
  zoomNormalAction->setEnabled(false);

  fitToWindowAction = new QAction("Fit to &window", this);
  fitToWindowAction->setShortcut(QKeySequence("Ctrl+1"));
  fitToWindowAction->setIcon(QIcon(":/fit_to_size.png"));
  fitToWindowAction->setStatusTip("Fit the image to window");
  QObject::connect(fitToWindowAction, SIGNAL(triggered()), this, SLOT(fitToWindow()));
  fitToWindowAction->setEnabled(false);
  fitToWindowAction->setCheckable(true);

  aboutAction = new QAction("&About...", this);
  aboutAction->setStatusTip("Display the about information");
  QObject::connect(aboutAction, SIGNAL(triggered()), this, SLOT(about()));

  aboutQtAction = new QAction("About &Qt...", this);
  aboutQtAction->setStatusTip("Display information about the Qt library");
  QObject::connect(aboutQtAction, SIGNAL(triggered()), QApplication::instance(),
                   SLOT(aboutQt()));
}

void ImageViewer::createMenus()
{
  QMenu *fileMenu = menuBar()->addMenu("&File");
  fileMenu->addAction(openAction);
  fileMenu->addAction(printAction);
  fileMenu->addSeparator();
  fileMenu->addAction(exitAction);

  QMenu *viewMenu = menuBar()->addMenu("&View");
  viewMenu->addAction(zoomInAction);
  viewMenu->addAction(zoomOutAction);
  viewMenu->addAction(zoomNormalAction);
  viewMenu->addSeparator();
  viewMenu->addAction(fitToWindowAction);

  QMenu *helpMenu = menuBar()->addMenu("Help");
  helpMenu->addAction(aboutAction);
  helpMenu->addAction(aboutQtAction);
}

void ImageViewer::createToolbar()
{
  QToolBar *toolBar = addToolBar("&Main");
  toolBar->addAction(openAction);
  toolBar->addAction(printAction);
  toolBar->addAction(zoomInAction);
  toolBar->addAction(zoomOutAction);
  toolBar->addAction(fitToWindowAction);
}

void ImageViewer::updateActions()
{
  fitToWindowAction->setEnabled(imageLoaded);
  zoomInAction->setEnabled(!fitToWindowAction->isChecked());
  zoomOutAction->setEnabled(!fitToWindowAction->isChecked());
  zoomNormalAction->setEnabled(!fitToWindowAction->isChecked());
}

void ImageViewer::scaleImage(double factor)
{
  scaleFactor *= factor;
  imageLabel->resize(scaleFactor * imageLabel->pixmap(Qt::ReturnByValue).size());

  adjustScrollBar(scrollArea->horizontalScrollBar(), factor);
  adjustScrollBar(scrollArea->verticalScrollBar(), factor);

  zoomInAction->setEnabled(scaleFactor < 5.0);
  zoomOutAction->setEnabled(scaleFactor > 0.10);
}

void ImageViewer::adjustScrollBar(QScrollBar *scrollBar, double factor)
{
  scrollBar->setValue(
    int(factor * scrollBar->value() + ((factor - 1) * scrollBar->pageStep() / 2)));
}

bool ImageViewer::loadImage(const QString &imagePath)
{
  QImageReader reader(imagePath);
  reader.setAutoTransform(true);
  const QImage newImage = reader.read();
  if (newImage.isNull()) {
    imageLoaded = false;
    QMessageBox::information(this, "ImageViewer",
                             QString("FATAL: could not load image %1").arg(imagePath));
    return false;
  }

  scaleFactor = 1.0;
  imageLoaded = true;
  scrollArea->setVisible(true);
  imageLabel->setPixmap(QPixmap::fromImage(newImage));
  imageLabel->adjustSize();

  QString title;
  QTextStream ostr(&title);
  ostr << "Qt " << QT_VERSION_STR << " ImageViewer: " << imagePath;
  setWindowTitle(title);

  return true;
}

void ImageViewer::initializeFileDialog(QFileDialog &dialog,
                                       QFileDialog::AcceptMode acceptMode)
{
  const QStringList picsLocation = QStandardPaths::standardLocations(
    QStandardPaths::PicturesLocation);
  dialog.setDirectory(picsLocation.isEmpty() ? QDir::currentPath() : picsLocation.last());

  QStringList mimeTypeFilters;
  const QByteArrayList supportedMimeTypes = (acceptMode == QFileDialog::AcceptOpen)
                                              ? QImageReader::supportedMimeTypes()
                                              : QImageWriter::supportedMimeTypes();
  for (const QByteArray &mimeTypeName : supportedMimeTypes)
    mimeTypeFilters.append(mimeTypeName);
  mimeTypeFilters.sort();
  dialog.setMimeTypeFilters(mimeTypeFilters);
  dialog.selectMimeTypeFilter("image/jpeg");
  dialog.setAcceptMode(acceptMode);
  if (acceptMode == QFileDialog::AcceptSave)
    dialog.setDefaultSuffix("jpg");
}

void ImageViewer::open()
{
  QFileDialog dialog(this, "Open Image");
  initializeFileDialog(dialog, QFileDialog::AcceptOpen);

  if (dialog.exec() == QFileDialog::Accepted
      && loadImage(dialog.selectedFiles().constFirst()))
    updateActions();
}

void ImageViewer::print()
{
  QMessageBox::information(this, "ImageViewer", "Implementation for Print Image");
}

void ImageViewer::zoomIn()
{
  scaleImage(1.25); // zoom in by 25%
}

void ImageViewer::zoomOut()
{
  scaleImage(0.75); // zoom out by 25%
}

void ImageViewer::normalSize()
{
  imageLabel->adjustSize();
  scaleFactor = 1.0;
}

void ImageViewer::fitToWindow()
{
  bool fitToWindow = fitToWindowAction->isChecked();
  scrollArea->setWidgetResizable(fitToWindow);
  if (!fitToWindow)
    normalSize();
  updateActions();
}

void ImageViewer::about()
{
  QString str = QString("<p><b>Image Viewer</b> application to view images on desktop.</p>"
                        "<p>Developed with Qt %1 by Manish Bhobe</p>"
                        "<p>Free to use, but use at your own risk!!")
                  .arg(QT_VERSION_STR);
  QMessageBox::about(this, tr("About Image Viewer"), str);
}
