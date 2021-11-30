// ============================================================================
// step07.cc: Adding actions + menus + signals and slots
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

  QFont font = QFont("SF UI Text", QApplication::font("QMenu").pointSize());
  app.setFont(font);

#ifdef Q_OS_WINDOWS
  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&app);
#endif

  // create the GUI
  DrawWindow mainWindow;
  mainWindow.setFont(font); 
  mainWindow.show();

  return app.exec();
}
