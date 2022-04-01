#include "ImageEditor.h"
#include "ImageSpinner.h"
#include "MatOps.h" // cv::Mat specific image operations
#include "common_funcs.h"
#include "ui_ImageEditor.h"
#include <opencv2/opencv.hpp>
#include <QtCore>
#include <QtGui>
#include <QtWidgets>

ImageEditor::ImageEditor(QWidget *parent)
   : QMainWindow(parent) /*, m_pixmap(nullptr) */, imageSpinner(nullptr)
{
   setWindowTitle(QString("Qt %1 Image Editor with Chocolaf").arg(QT_VERSION_STR));
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
   statusBar()->showMessage(QString("ImageViewer with Qt %1 and Chocolaf theme").arg(QT_VERSION_STR));

   // set initial size to 4/5 of screen
   resize(QGuiApplication::primaryScreen()->availableSize() * 4 / 5);
   setWindowIcon(QIcon(":/ImageEditor-icon.png")); // set the main window icon
}

ImageEditor::~ImageEditor() {}

// helper function
QString getIconPath(QString baseName, bool darkTheme = false)
{
   QString iconPath = QString(":/%1_%2.png").arg(baseName).arg(darkTheme ? "dark" : "light");
   qDebug() << "Loading icon " << iconPath;
   return iconPath;
}

void ImageEditor::createActions()
{
   bool usingDarkTheme = true;
   openAction = new QAction("&Open...", this);
   openAction->setShortcut(QKeySequence::Open);
   // openAction->setIcon(QIcon(":/open.png"));
   openAction->setIcon(QIcon(getIconPath("open", usingDarkTheme)));
   openAction->setStatusTip("Open a new image file to view");
   QObject::connect(openAction, SIGNAL(triggered()), this, SLOT(open()));

   printAction = new QAction("&Print...", this);
   printAction->setShortcut(QKeySequence::Print);
   // printAction->setIcon(QIcon(":/print.png"));
   printAction->setIcon(QIcon(getIconPath("print", usingDarkTheme)));
   printAction->setStatusTip("Print the current image");
   QObject::connect(printAction, SIGNAL(triggered()), this, SLOT(print()));
   printAction->setEnabled(false);

   exitAction = new QAction("E&xit", this);
   exitAction->setShortcut(QKeySequence("Ctrl+Q"));
   exitAction->setStatusTip("Quit the application");
   QObject::connect(exitAction, SIGNAL(triggered()), QApplication::instance(), SLOT(quit()));

   blurAction = new QAction("&Blur Image", this);
   blurAction->setIcon(QIcon(getIconPath("blur", usingDarkTheme)));
   blurAction->setStatusTip("Blue active image");
   QObject::connect(blurAction, SIGNAL(triggered()), this, SLOT(blurImage()));
   blurAction->setEnabled(false);

   sharpenAction = new QAction("&Sharpen Image", this);
   sharpenAction->setIcon(QIcon(getIconPath("sharpen", usingDarkTheme)));
   sharpenAction->setStatusTip("Sharpen active image");
   QObject::connect(sharpenAction, SIGNAL(triggered()), this, SLOT(sharpenImage()));
   sharpenAction->setEnabled(false);

   erodeAction = new QAction("&Erode Image", this);
   erodeAction->setIcon(QIcon(getIconPath("erode", usingDarkTheme)));
   erodeAction->setStatusTip("Erode active image");
   QObject::connect(erodeAction, SIGNAL(triggered()), this, SLOT(erodeImage()));
   erodeAction->setEnabled(false);

   zoomInAction = new QAction("Zoom &in (25%)", this);
   zoomInAction->setShortcut(QKeySequence("Ctrl++"));
   // zoomInAction->setIcon(QIcon(":/zoom_in.png"));
   zoomInAction->setIcon(QIcon(getIconPath("zoomin", usingDarkTheme)));
   zoomInAction->setStatusTip("Zoom into the image by 25%");
   QObject::connect(zoomInAction, SIGNAL(triggered()), this, SLOT(zoomIn()));
   zoomInAction->setEnabled(false);

   zoomOutAction = new QAction("Zoom &out (25%)", this);
   zoomOutAction->setShortcut(QKeySequence("Ctrl+-"));
   // zoomOutAction->setIcon(QIcon(":/zoom_out.png"));
   zoomOutAction->setIcon(QIcon(getIconPath("zoomout", usingDarkTheme)));
   zoomOutAction->setStatusTip("Zoom out of the image by 25%");
   QObject::connect(zoomOutAction, SIGNAL(triggered()), this, SLOT(zoomOut()));
   zoomOutAction->setEnabled(false);

   fitToWindowAction = new QAction("Fit to &window", this);
   fitToWindowAction->setShortcut(QKeySequence("Ctrl+1"));
   // fitToWindowAction->setIcon(QIcon(":/fit_to_size.png"));
   fitToWindowAction->setIcon(QIcon(getIconPath("fit_to_size", usingDarkTheme)));
   fitToWindowAction->setStatusTip("Fit the image to window");
   QObject::connect(fitToWindowAction, SIGNAL(triggered()), this, SLOT(fitToWindow()));
   fitToWindowAction->setEnabled(false);
   fitToWindowAction->setCheckable(true);

   prevImageAction = new QAction("&Previous image", this);
   prevImageAction->setShortcut(QKeySequence::MoveToPreviousChar); // left arrow (usually)
   // prevImageAction->setIcon(QIcon(":/previous.png"));
   prevImageAction->setIcon(QIcon(getIconPath("prev", usingDarkTheme)));
   prevImageAction->setStatusTip("View previous image in folder");
   QObject::connect(prevImageAction, SIGNAL(triggered()), this, SLOT(prevImage()));
   prevImageAction->setEnabled(false);

   nextImageAction = new QAction("&Next image", this);
   nextImageAction->setShortcut(QKeySequence::MoveToNextChar); // right arrow (usually)
   // nextImageAction->setIcon(QIcon(":/next.png"));
   nextImageAction->setIcon(QIcon(getIconPath("next", usingDarkTheme)));
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

void ImageEditor::createMenus()
{
   QMenu *fileMenu = menuBar()->addMenu("&File");
   fileMenu->addAction(openAction);
   fileMenu->addAction(printAction);
   fileMenu->addSeparator();
   fileMenu->addAction(exitAction);

   QMenu *editMenu = menuBar()->addMenu("&Edit");
   editMenu->addAction(blurAction);
   editMenu->addAction(sharpenAction);
   editMenu->addAction(erodeAction);

   QMenu *viewMenu = menuBar()->addMenu("&View");
   viewMenu->addAction(zoomInAction);
   viewMenu->addAction(zoomOutAction);
   //viewMenu->addAction(zoomNormalAction);
   viewMenu->addSeparator();
   viewMenu->addAction(fitToWindowAction);
   viewMenu->addSeparator();
   viewMenu->addAction(prevImageAction);
   viewMenu->addAction(nextImageAction);

   QMenu *helpMenu = menuBar()->addMenu("Help");
   helpMenu->addAction(aboutAction);
   helpMenu->addAction(aboutQtAction);
}

void ImageEditor::createToolbar()
{
   QToolBar *toolBar = addToolBar("&Main");

   toolBar->addAction(openAction);
   toolBar->addAction(printAction);
   toolBar->addSeparator();

   toolBar->addAction(blurAction);
   toolBar->addAction(sharpenAction);
   toolBar->addAction(erodeAction);
   toolBar->addSeparator();

   toolBar->addAction(zoomInAction);
   toolBar->addAction(zoomOutAction);
   toolBar->addAction(fitToWindowAction);
   toolBar->addAction(prevImageAction);
   toolBar->addAction(nextImageAction);
}

void ImageEditor::updateActions()
{
   blurAction->setEnabled(imageLoaded);
   sharpenAction->setEnabled(imageLoaded);
   erodeAction->setEnabled(imageLoaded);

   fitToWindowAction->setEnabled(imageLoaded);
   zoomInAction->setEnabled(!fitToWindowAction->isChecked());
   zoomOutAction->setEnabled(!fitToWindowAction->isChecked());
   //zoomNormalAction->setEnabled(!fitToWindowAction->isChecked());
   prevImageAction->setEnabled(imageLoaded);
   nextImageAction->setEnabled(imageLoaded);
}

void ImageEditor::writeSettings()
{
   QSettings settings("QtPie Apps Inc.", "ImageEditor - OpenCV");

   settings.beginGroup("mainWindow");
   settings.setValue("geometry", saveGeometry());
   settings.setValue("state", saveState());
   settings.endGroup();
   qDebug() << "ImageEditor settings saved";
}

void ImageEditor::readSettings()
{
   QSettings settings("QtPie Apps Inc.", "ImageEditor - OpenCV");

   settings.beginGroup("mainWindow");
   restoreGeometry(settings.value("geometry").toByteArray());
   restoreState(settings.value("state").toByteArray());
   settings.endGroup();
   qDebug() << "ImageEditor settings loaded";
}

void ImageEditor::scaleImage(double factor)
{
   scaleFactor *= factor;
   imageLabel->resize(scaleFactor * imageLabel->pixmap(Qt::ReturnByValue).size());

   adjustScrollBar(scrollArea->horizontalScrollBar(), factor);
   adjustScrollBar(scrollArea->verticalScrollBar(), factor);

   zoomInAction->setEnabled(scaleFactor < 5.0);
   zoomOutAction->setEnabled(scaleFactor > 0.10);
}

void ImageEditor::adjustScrollBar(QScrollBar *scrollBar, double factor)
{
   scrollBar->setValue(int(factor * scrollBar->value() + ((factor - 1) * scrollBar->pageStep() / 2)));
}

bool ImageEditor::loadImage(const QString &imagePath)
{
   QImageReader reader(imagePath);
   reader.setAutoTransform(true);
   const QImage newImage = reader.read();
   if (newImage.isNull()) {
      imageLoaded = false;
      QMessageBox::information(this, "ImageEditor", QString("FATAL: could not load image %1").arg(imagePath));
      return false;
   }

   scaleFactor = 1.0;
   imageLoaded = true;
   scrollArea->setVisible(true);
   imageLabel->setPixmap(QPixmap::fromImage(newImage));
   imageLabel->adjustSize();

   QString title;
   QTextStream ostr(&title);
   ostr << "Qt " << QT_VERSION_STR << " ImageEditor: " << imagePath;
   setWindowTitle(title);

   // add ImageSpinner
   delete imageSpinner;
   imageSpinner = new ImageSpinner(imagePath);

   return true;
}

void ImageEditor::initializeFileDialog(QFileDialog &dialog, QFileDialog::AcceptMode acceptMode)
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

void ImageEditor::open()
{
   QFileDialog dialog(this, "Open Image");
   initializeFileDialog(dialog, QFileDialog::AcceptOpen);
   if (dialog.exec() == QFileDialog::Accepted && loadImage(dialog.selectedFiles().constFirst()))
      updateActions();
}

void ImageEditor::print()
{
   QMessageBox::information(this, "ImageEditor", "TODO: Implementation for Print Image");
}

void ImageEditor::blurImage()
{
   // qDebug() << "This will blur the image...";
   if (imageLoaded) {
      MatOp blurOp(*(imageLabel->pixmap()));
      imageLabel->setPixmap(blurOp.blur());
      imageLabel->adjustSize();
   }
   else
      qDebug() << "blurImage() should not be called if image is not loaded!";
}

void ImageEditor::sharpenImage()
{
   if (imageLoaded) {
      MatOp sharpenOp(*(imageLabel->pixmap()));
      imageLabel->setPixmap(sharpenOp.sharpen());
      imageLabel->adjustSize();
   }
   else
      qDebug() << "sharpenImage() should not be called if image is not loaded!";
}

void ImageEditor::erodeImage()
{
   if (imageLoaded) {
      MatOp erodeOp(*(imageLabel->pixmap()));
      imageLabel->setPixmap(erodeOp.erode());
      imageLabel->adjustSize();
   }
   else
      qDebug() << "erodeImage() should not be called if image is not loaded!";
}

void ImageEditor::zoomIn()
{
   scaleImage(1.25); // zoom in by 25%
}

void ImageEditor::zoomOut()
{
   scaleImage(0.75); // zoom out by 25%
}

void ImageEditor::normalSize()
{
   imageLabel->adjustSize();
   scaleFactor = 1.0;
}

void ImageEditor::fitToWindow()
{
   bool fitToWindow = fitToWindowAction->isChecked();
   scrollArea->setWidgetResizable(fitToWindow);
   if (!fitToWindow)
      normalSize();
   updateActions();
}

void ImageEditor::prevImage()
{
   QString imagePath = imageSpinner->prevImage();
   if (loadImage(imagePath))
      updateActions();
   if (imageSpinner->atFirst())
      QMessageBox::information(this, "ImageEditor", "Displaying first image in folder!");
}

void ImageEditor::nextImage()
{
   QString imagePath = imageSpinner->nextImage();
   if (loadImage(imagePath))
      updateActions();
   if (imageSpinner->atLast())
      QMessageBox::information(this, "ImageEditor", "Displaying last image in folder!");
}

void ImageEditor::about()
{
   QString str = QString(
                    "<p><b>Image Viewer</b> application to view images on desktop.</p>"
                    "<p>Developed with Qt %1 by Manish Bhobe</p>"
                    "<p>Uses Chocolaf dark theme for Windows & Linux</p>"
                    "<p>Free to use, but use at your own risk!!")
                    .arg(QT_VERSION_STR);
   QMessageBox::about(this, tr("About Image Viewer"), str);
}
