// ============================================================================
// step02.cc: Handling events in the main window
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================

#include <QApplication>
#include <QtGui>
#include "DrawWindow.h"

int main(int argc, char **argv)
{
  QApplication app(argc, argv);

  // create the GUI
  DrawWindow mainWindow;
  mainWindow.show();

  return app.exec();
}

