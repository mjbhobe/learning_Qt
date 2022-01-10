#include "ImageViewer.h"
#include "ui_ImageViewer.h"
#include <QtCore>
#include <QtGui>
#include <QtWidgets>

ImageSpinner::ImageSpinner(const QString &imagePath) : m_currIndex(-1)
{
   QFileInfo current(imagePath);
   m_dir = current.absoluteDir();
   QStringList imageFilters;
   imageFilters << "*.tiff"
                << "*.tif"
                << "*.jpg"
                << "*.jpeg"
                << "*.gif"
                << "*.bmp"
                << "*.png";
   m_fileNames = m_dir.entryList(imageFilters, QDir::Files, QDir::Name);
   m_currIndex = m_fileNames.indexOf(QRegExp(QRegExp::escape(current.fileName())));
}

QString ImageSpinner::prevImage()
{
   m_currIndex = m_currIndex - 1;
   if (m_currIndex < 0)
      m_currIndex = 0; // keep at 0th index
   QString prevImagePath = m_dir.absolutePath() + QDir::separator() + m_fileNames.at(m_currIndex);
   qDebug() << "Will display (prev): " << prevImagePath;
   //return dir.absoluteFilePath(m_fileNames.at(m_currIndex));
   return prevImagePath;
}

QString ImageSpinner::nextImage()
{
   m_currIndex = m_currIndex + 1;
   if (m_currIndex > m_fileNames.count() - 1)
      m_currIndex = m_fileNames.count() - 1; // keep at last index

   QString nextImagePath = m_dir.absolutePath() + QDir::separator() + m_fileNames.at(m_currIndex);
   qDebug() << "Will display (next): " << nextImagePath;
   //return dir.absoluteFilePath(m_fileNames.at(m_currIndex));
   return nextImagePath;
}

bool ImageSpinner::atFirst() const
{
   return m_currIndex == 0;
}

bool ImageSpinner::atLast() const
{
   return m_currIndex == m_fileNames.count() - 1;
}

ImageViewer::ImageViewer(QWidget *parent) : QMainWindow(parent), image(nullptr), imageSpinner(nullptr)
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
   createToolbars();
   statusBar()->showMessage("");
   statusBar()->setStyleSheet(
      "QStatusBar{padding-left:8px;background:rgb(59,59,59);color:rgb(127,127,127);}");

   // set initial size to 3/5 of screen
   resize(QGuiApplication::primaryScreen()->availableSize() * 4 / 5);
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

   prevImageAction = new QAction("&Previous image", this);
   prevImageAction->setShortcut(QKeySequence::MoveToPreviousChar); // left arrow (usually)
   prevImageAction->setIcon(QIcon(":/previous.png"));
   prevImageAction->setStatusTip("View previous image in folder");
   QObject::connect(prevImageAction, SIGNAL(triggered()), this, SLOT(prevImage()));
   prevImageAction->setEnabled(false);

   nextImageAction = new QAction("&Next image", this);
   nextImageAction->setShortcut(QKeySequence::MoveToNextChar); // right arrow (usually)
   nextImageAction->setIcon(QIcon(":/next.png"));
   nextImageAction->setStatusTip("View next image in folder");
   QObject::connect(nextImageAction, SIGNAL(triggered()), this, SLOT(nextImage()));
   nextImageAction->setEnabled(false);

   aboutAction = new QAction("&About...", this);
   aboutAction->setStatusTip("Display the about information");
   QObject::connect(aboutAction, SIGNAL(triggered()), this, SLOT(about()));

   aboutQtAction = new QAction("About &Qt...", this);
   aboutQtAction->setStatusTip("Display information about the Qt library");
   QObject::connect(aboutQtAction, SIGNAL(triggered()), QApplication::instance(), SLOT(aboutQt()));
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
   viewMenu->addSeparator();
   viewMenu->addAction(prevImageAction);
   viewMenu->addAction(nextImageAction);

   QMenu *helpMenu = menuBar()->addMenu("Help");
   helpMenu->addAction(aboutAction);
   helpMenu->addAction(aboutQtAction);
}

void ImageViewer::createToolbars()
{
   QToolBar *toolBar = addToolBar("&Main");
   QPalette palette = toolBar->palette();
   palette.setColor(QPalette::Window, QColor(59, 59, 59));
   toolBar->setPalette(palette);
   toolBar->addAction(openAction);
   toolBar->addAction(printAction);

   QToolBar *toolBar2 = addToolBar("&View");
   palette = toolBar2->palette();
   palette.setColor(QPalette::Window, QColor(59, 59, 59));
   toolBar2->addAction(zoomInAction);
   toolBar2->addAction(zoomOutAction);
   toolBar2->addAction(fitToWindowAction);
   toolBar2->addAction(prevImageAction);
   toolBar2->addAction(nextImageAction);
}

void ImageViewer::updateActions()
{
   fitToWindowAction->setEnabled(imageLoaded);
   zoomInAction->setEnabled(!fitToWindowAction->isChecked());
   zoomOutAction->setEnabled(!fitToWindowAction->isChecked());
   zoomNormalAction->setEnabled(!fitToWindowAction->isChecked());
   prevImageAction->setEnabled(imageLoaded);
   nextImageAction->setEnabled(imageLoaded);
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
   scrollBar->setValue(int(factor * scrollBar->value() + ((factor - 1) * scrollBar->pageStep() / 2)));
}

bool ImageViewer::loadImage(const QString &imagePath)
{
   QImageReader reader(imagePath);
   reader.setAutoTransform(true);
   const QImage newImage = reader.read();
   if (newImage.isNull()) {
      imageLoaded = false;
      QMessageBox::information(this, "ImageViewer", QString("FATAL: could not load image %1").arg(imagePath));
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

   // add ImageSpinner
   delete imageSpinner;
   imageSpinner = new ImageSpinner(imagePath);

   return true;
}

void ImageViewer::initializeFileDialog(QFileDialog &dialog, QFileDialog::AcceptMode acceptMode)
{
   const QStringList picsLocation = QStandardPaths::standardLocations(QStandardPaths::PicturesLocation);
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

   if (dialog.exec() == QFileDialog::Accepted && loadImage(dialog.selectedFiles().constFirst()))
      updateActions();
}

void ImageViewer::print()
{
   QMessageBox::information(this, "ImageViewer", "TODO: Implementation for Print Image");
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

void ImageViewer::prevImage()
{
   QString imagePath = imageSpinner->prevImage();
   if (loadImage(imagePath))
      updateActions();
   if (imageSpinner->atFirst())
      QMessageBox::information(this, "ImageViewer", "Displaying first image in folder!");
}

void ImageViewer::nextImage()
{
   QString imagePath = imageSpinner->nextImage();
   if (loadImage(imagePath))
      updateActions();
   if (imageSpinner->atLast())
      QMessageBox::information(this, "ImageViewer", "Displaying last image in folder!");
}

void ImageViewer::about()
{
   QString str = QString("<p><b>Image Viewer</b> application to view images on desktop.</p>"
                         "<p>Developed with Qt %1 by Manish Bhobe</p>"
                         "<p>Free to use, but use at your own risk!!")
                    .arg(QT_VERSION_STR);
   QMessageBox::about(this, tr("About Image Viewer"), str);
}
