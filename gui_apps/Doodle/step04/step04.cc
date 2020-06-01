// ============================================================================
// step01.cc: Drawing single lines in the main window
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================

#include "DrawWindow.h"
#include <QApplication>
#include <QtGui>

int main(int argc, char **argv)
{
  QApplication app(argc, argv);

  // create the GUI
  DrawWindow mainWindow;
  mainWindow.show();

  return app.exec();
}
