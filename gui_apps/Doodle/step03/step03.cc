// ============================================================================
// step03.cc: Drawing in the main window
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================
#include <QApplication>
#include <QMainWindow>
#include <QtGui>
#include "DrawWindow.h"

const QString AppTitle("Qt Scribble");
const QString WinTitle("Qt Scribble - Step03: Handling mouse clicks");

int main(int argc, char **argv) {
  QApplication app(argc, argv);

  // create the GUI
  QMainWindow mainWindow;
  mainWindow.setWindowTitle(WinTitle);
  DrawWindow *drawWindow = new DrawWindow;
  mainWindow.setCentralWidget(drawWindow);
  mainWindow.resize(640, 480);
  mainWindow.show();

  return app.exec();
}
