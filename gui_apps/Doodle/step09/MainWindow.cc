// MainWindow.cc: implements MainWindow class
#include "MainWindow.h"
#include "DrawWindow.h"
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

   createActions();
   createMenus();
   createToolBar();
   createStatusBar();

   QObject::connect(_drawWindow, SIGNAL(doodleModified2(bool)), this, SLOT(doodleModified(bool)));
   setCentralWidget(_drawWindow);
   resize(640, 480);
   doodleModified(false);
}

void MainWindow::createActions()
{
   Q_ASSERT(_drawWindow != nullptr);
   fileNewAction = new QAction(QIcon(":/images/fileNew.png"), tr("&New"), this);
   fileNewAction->setShortcut(tr("Ctrl+N"));
   fileNewAction->setStatusTip(tr("Create a new scribble document."));
   QObject::connect(fileNewAction, SIGNAL(triggered()), _drawWindow, SLOT(fileNew()));

   fileOpenAction = new QAction(QIcon(":/images/fileOpen.png"), tr("&Open..."), this);
   fileOpenAction->setShortcut(tr("Ctrl+O"));
   fileOpenAction->setStatusTip(tr("Open scribble document from disk file."));
   QObject::connect(fileOpenAction, SIGNAL(triggered()), _drawWindow, SLOT(fileOpen()));

   fileSaveAction = new QAction(QIcon(":/images/fileSave.png"), tr("&Save"), this);
   fileSaveAction->setShortcut(tr("Ctrl+S"));
   fileSaveAction->setStatusTip(tr("Save scribble document to disk file."));
   QObject::connect(fileSaveAction, SIGNAL(triggered()), _drawWindow, SLOT(fileSave()));

   fileSaveAsAction = new QAction(QIcon(":/images/fileSaveAs.png"), tr("Save &as..."), this);
   fileSaveAsAction->setStatusTip(tr("Save scribble document to disk with different name."));
   QObject::connect(fileSaveAsAction, SIGNAL(triggered()), _drawWindow, SLOT(fileSaveAs()));

   exitAction = new QAction(QIcon(":/images/exit.png"), tr("E&xit"), this);
   exitAction->setStatusTip(tr("Save all pending changes and quit application."));
   QObject::connect(exitAction, SIGNAL(triggered()), this, SLOT(exitApp()));

   penWidthAction = new QAction(
      QIcon(":/images/lineThickness.png"), tr("Change pen &width..."), this);
   penWidthAction->setShortcut(tr("Ctrl+W"));
   penWidthAction->setStatusTip(tr("Change the width of default pen."));
   QObject::connect(penWidthAction, SIGNAL(triggered()), _drawWindow, SLOT(changePenWidth()));

   penColorAction = new QAction(QIcon(":/images/lineColor.png"), tr("Change pen &color..."), this);
   penColorAction->setShortcut(tr("Ctrl+L"));
   penColorAction->setStatusTip(tr("Change the color of default pen."));
   QObject::connect(penColorAction, SIGNAL(triggered()), _drawWindow, SLOT(changePenColor()));

   aboutAction = new QAction(QIcon(":/images/about.png"), tr("&About..."), this);
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
   close();
}

void MainWindow::about()
{
   QString msg;
   QTextStream ostr(&msg);

   ostr << "Qt Scribble\n\n"
        << "Doodling app (based on Borland ObjectWindows Tutorial)\n"
        << "Built with Qt Framework version " << QT_VERSION_STR << "\n"
        << "Written by - Manish Bhobe";

   QMessageBox::information(this, AppTitle, msg);
}

void MainWindow::doodleModified(bool modified)
{
   fileSaveAction->setEnabled(modified);
   QString winTitle;
   QTextStream ostr(&winTitle);
   ostr << WindowTitle << " - [" << _drawWindow->getDoodle()->filePath() << "]"
        << (modified ? "*" : "");
   setWindowTitle(winTitle);
}
