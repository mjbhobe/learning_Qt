// ============================================================================
// step02.cc: Handling events in the main window
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================

#include <QApplication>
#include <QtGui>
#include "common.hxx"
#include "DrawWindow.h"

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

