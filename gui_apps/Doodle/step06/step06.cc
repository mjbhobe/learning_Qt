// ============================================================================
// step06.cc: Adding collection of lines to doodle + loading & saving lines
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================

#include <QApplication>
#include <QtGui>
#include "DrawWindow.h"
#include "common.hxx"

int main(int argc, char **argv)
{
  QApplication app(argc, argv);
  app.setStyle("Fusion");

#ifdef Q_OS_WINDOWS
  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&app);
#endif

  // create the GUI
  DrawWindow mainWindow;
  mainWindow.show();

  return app.exec();
}

