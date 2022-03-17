// ============================================================================
// step08.cc: Loading & saving collection of lines
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================

#include <QApplication>
#include <QtGui>
#include "MainWindow.h"
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
  MainWindow mainWindow;
  mainWindow.show();

  return app.exec();
}

