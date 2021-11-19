// ============================================================================
// step05.cc: drawing single lines in window, but with their separate attributes
// of line width & color.
// 	- double left mouse click - set line width
//  - double right mouse click - set line color
//    (NOTE: this is an absolutely horrible GUI design!! Purpose of this code is not
//     to present a good GUI design, rather to be able to set line width & color.
//     This flaw will be corrected in further tutorials).
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================

#include "DrawWindow.h"
#include "common.hxx"
#include <QApplication>
#include <QtGui>

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
