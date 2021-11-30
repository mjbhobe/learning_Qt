// MainWindow.cc: implements MainWindow class
#include "MainWindow.h"
#include "DrawWindow.h"
#include "common.hxx"
#include <QAction>
#include <QMainWindow>
#include <QMenu>
#include <QMenuBar>
#include <QMessageBox>
#include <QStatusBar>
#include <QTextStream>
#include <QToolBar>

const QString AppTitle("Qt Scribble");
const QString WindowTitle("Qt Scribble - Step09: Adding Toolbar & Statusbar");

MainWindow::MainWindow()
{
   setWindowTitle(WindowTitle);
   _drawWindow = new DrawWindow();
   setWindowIcon(QIcon(":/icons/appIcon.png"));

   createActions();
   createMenus();
   createToolBar();
   createStatusBar();
   statusBar()->showMessage("Qt Scribble - Doodling Application. Created by Manish Bhobe");

   QObject::connect(_drawWindow, SIGNAL(doodleModified2(bool)), this, SLOT(doodleModified(bool)));
   setCentralWidget(_drawWindow);
   // resize(640, 480);
   resize(QGuiApplication::primaryScreen()->availableSize() * 3 / 5);
   // set timer to change palette between dark & light palettes
   this->_timerId = this->startTimer(1000);
   doodleModified(false);
}

void MainWindow::timerEvent(QTimerEvent *e)
{
   if (e->timerId() == this->_timerId) {
#ifdef Q_OS_WINDOWS
      if (windowsDarkThemeAvailable() && windowsIsInDarkTheme()) {
         // set my custom dark palette
         setWinDarkPalette(qApp);
         qDebug() << "Timer Id: " << e->timerId() << " fired! Dark palette set!";
      } else {
         // set default light palette
         // @see: https://stackoverflow.com/questions/31848671/how-to-set-qpalette-back-to-default-system-palette
         // qApp->setPalette(qApp->style()->standardPalette());
         qApp->setStyleSheet("");
         qDebug() << "Timer Id: " << e->timerId() << " fired! Light palette set!";
      }
      //_drawWindow->resizeImage(QSize(_drawWindow->width(), _drawWindow->height()), true);
      _drawWindow->clearImage(false);
      update();
#endif
   }
}

void MainWindow::createActions()
{
   Q_ASSERT(_drawWindow != nullptr);
   fileNewAction = new QAction(QIcon(":/icons/fileNew.png"), tr("&New"), this);
   fileNewAction->setShortcut(tr("Ctrl+N"));
   fileNewAction->setStatusTip(tr("Create a new scribble document."));
   QObject::connect(fileNewAction, SIGNAL(triggered()), _drawWindow, SLOT(fileNew()));

   fileOpenAction = new QAction(QIcon(":/icons/fileOpen.png"), tr("&Open..."), this);
   fileOpenAction->setShortcut(tr("Ctrl+O"));
   fileOpenAction->setStatusTip(tr("Open scribble document from disk file."));
   QObject::connect(fileOpenAction, SIGNAL(triggered()), _drawWindow, SLOT(fileOpen()));

   fileSaveAction = new QAction(QIcon(":/icons/fileSave.png"), tr("&Save"), this);
   fileSaveAction->setShortcut(tr("Ctrl+S"));
   fileSaveAction->setStatusTip(tr("Save scribble document to disk file."));
   QObject::connect(fileSaveAction, SIGNAL(triggered()), _drawWindow, SLOT(fileSave()));

   fileSaveAsAction = new QAction(QIcon(":/icons/fileSaveAs.png"), tr("Save &as..."), this);
   fileSaveAsAction->setStatusTip(tr("Save scribble document to disk with different name."));
   QObject::connect(fileSaveAsAction, SIGNAL(triggered()), _drawWindow, SLOT(fileSaveAs()));

   exitAction = new QAction(QIcon(":/icons/exit.png"), tr("E&xit"), this);
   exitAction->setStatusTip(tr("Save all pending changes and quit application."));
   QObject::connect(exitAction, SIGNAL(triggered()), this, SLOT(exitApp()));

   penWidthAction = new QAction(QIcon(":/icons/lineThickness.png"), tr("Change pen &width..."), this);
   penWidthAction->setShortcut(tr("Ctrl+W"));
   penWidthAction->setStatusTip(tr("Change the width of default pen."));
   QObject::connect(penWidthAction, SIGNAL(triggered()), _drawWindow, SLOT(changePenWidth()));

   penColorAction = new QAction(QIcon(":/icons/lineColor.png"), tr("Change pen &color..."), this);
   penColorAction->setShortcut(tr("Ctrl+L"));
   penColorAction->setStatusTip(tr("Change the color of default pen."));
   QObject::connect(penColorAction, SIGNAL(triggered()), _drawWindow, SLOT(changePenColor()));

   aboutQtAction = new QAction(tr("&About Qt..."), this);
   aboutQtAction->setStatusTip(tr("Display information Qt Library used."));
   QObject::connect(aboutQtAction, SIGNAL(triggered()), qApp, SLOT(aboutQt()));

   aboutAction = new QAction(QIcon(":/icons/about.png"), tr("&About..."), this);
   aboutAction->setStatusTip(tr("Display information about program."));
   QObject::connect(aboutAction, SIGNAL(triggered()), this, SLOT(about()));
}

void MainWindow::createMenus()
{
   fileMenu = new QMenu(tr("&File"), this);
   fileMenu->addAction(fileNewAction);
   fileMenu->addAction(fileOpenAction);
   fileMenu->addAction(fileSaveAction);
   fileMenu->addAction(fileSaveAsAction);
   fileMenu->addSeparator();
   fileMenu->addAction(exitAction);

   optionsMenu = new QMenu(tr("&Options"), this);
   optionsMenu->addAction(penWidthAction);
   optionsMenu->addAction(penColorAction);

   helpMenu = new QMenu(tr("&Help"), this);
   helpMenu->addAction(aboutQtAction);
   helpMenu->addAction(aboutAction);

   menuBar()->addMenu(fileMenu);
   menuBar()->addMenu(optionsMenu);
   menuBar()->addMenu(helpMenu);
}

void MainWindow::createToolBar()
{
   QToolBar *toolBar = new QToolBar(tr("Main"), this);
   toolBar->addAction(fileNewAction);
   toolBar->addAction(fileOpenAction);
   toolBar->addAction(fileSaveAction);
   toolBar->addAction(fileSaveAsAction);
   toolBar->addSeparator();
   toolBar->addAction(penWidthAction);
   toolBar->addAction(penColorAction);
   toolBar->addSeparator();
   toolBar->addAction(aboutAction);
   addToolBar(toolBar);
}

void MainWindow::createStatusBar()
{
   // the first call to statusBar() automatically creates one!
   statusBar()->showMessage(WindowTitle);
}

void MainWindow::exitApp()
{
   this->killTimer(this->_timerId);
   close();
}

void MainWindow::about()
{
   QString str;
   QTextStream ostr(&str);
   ostr << "<html><b>Qt Scribble</b> - Doodling application<p/>Developed with the Qt " << QT_VERSION_STR
        << " C++ framework.<p/><p/>Written by - Manish Bhobe.<p/><p/>"
        << "<small>Program developed for illustration purposes only! Use at your own "
        << "risk! Author is not responsible for any damages (direct or indirect) that "
        << "may result from the use of this program.</small></html>";
   QMessageBox::information(this, AppTitle, str);
}

void MainWindow::doodleModified(bool modified)
{
   fileSaveAction->setEnabled(modified);
   QString winTitle;
   QTextStream ostr(&winTitle);
   ostr << WindowTitle << " - [" << _drawWindow->getDoodle()->filePath() << "]" << (modified ? "*" : "");
   setWindowTitle(winTitle);
}
