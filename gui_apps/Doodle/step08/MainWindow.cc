// MainWindow.cc: implements MainWindow class
#include <QMainWindow>
#include <QAction>
#include <QMenu>
#include <QMenuBar>
#include <QMessageBox>
#include "MainWindow.h"
#include "DrawWindow.h"

const QString AppTitle("Qt Scribble");
const QString WindowTitle("Qt Scribble - Step08: Loading & Saving files");

MainWindow::MainWindow()
{
  setWindowTitle(WindowTitle);
  _drawWindow = new DrawWindow();

  createActions();
  createMenus();

  setCentralWidget(_drawWindow);
  resize(640,480);
}

void MainWindow::createActions()
{
  Q_ASSERT(_drawWindow != 0);
  fileNewAction = new QAction(QIcon(":/images/fileNew.jpeg"),tr("&New"),this);
  fileNewAction->setShortcut( tr("Ctrl+N"));
  fileNewAction->setStatusTip(tr("Create a new scribble document."));
  QObject::connect(fileNewAction, SIGNAL(triggered()), _drawWindow, SLOT(fileNew()));

  fileOpenAction = new QAction(QIcon(":/images/fileOpen.jpeg"),tr("&Open..."),this);
  fileOpenAction->setShortcut( tr("Ctrl+O"));
  fileOpenAction->setStatusTip(tr("Open scribble document from disk file."));
  QObject::connect(fileOpenAction, SIGNAL(triggered()), _drawWindow, SLOT(fileOpen()));

  fileSaveAction = new QAction(QIcon(":/images/fileSave.jpeg"),tr("&Save"),this);
  fileSaveAction->setShortcut( tr("Ctrl+S"));
  fileSaveAction->setStatusTip(tr("Save scribble document to disk file."));
  QObject::connect(fileSaveAction, SIGNAL(triggered()), _drawWindow, SLOT(fileSave()));

  fileSaveAsAction = new QAction(QIcon(":/images/fileSaveAs.jpeg"),tr("Save &as..."),this);
  fileSaveAsAction->setStatusTip(tr("Save scribble document to disk with different name."));
  QObject::connect(fileSaveAsAction, SIGNAL(triggered()), _drawWindow, SLOT(fileSaveAs()));

  exitAction = new QAction(tr("E&xit"),this);
  exitAction->setStatusTip(tr("Save all pending changes and quit application."));
  QObject::connect(exitAction, SIGNAL(triggered()), this, SLOT(exitApp()));

  penWidthAction = new QAction(tr("Change pen &width..."),this);
  penWidthAction->setStatusTip(tr("Change the width of default pen."));
  QObject::connect(penWidthAction, SIGNAL(triggered()), _drawWindow, SLOT(changePenWidth()));

  penColorAction = new QAction(tr("Change pen &color..."),this);
  penColorAction->setStatusTip(tr("Change the color of default pen."));
  QObject::connect(penColorAction, SIGNAL(triggered()), _drawWindow, SLOT(changePenColor()));

  aboutAction = new QAction(tr("&About..."),this);
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

void MainWindow::exitApp()
{
  close();
}

void MainWindow::about()
{
  QMessageBox::information(this, AppTitle, 
      tr("Qt Scribble\nScribble application developed with the Qt Framework\n"
         "Written by - Manish Bhobe"));
}

  

