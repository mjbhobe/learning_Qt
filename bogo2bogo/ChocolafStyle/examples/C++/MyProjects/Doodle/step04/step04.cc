// ============================================================================
// step01.cc: draw a single squiggle in the main window
//   click the left mouse & drag around the window to draw squiggle/doodle.
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
//
// @author Manish Bhobe for Nämostuté Ltd.
// My experiments with C++,Qt, Python & PyQt.
// Code is provided for illustration purposes only! Use at your own risk.
// =============================================================================

#include "DrawWindow.h"
#include "chocolaf.h"
#include <QApplication>
#include <QtGui>

int main(int argc, char **argv)
{
   Chocolaf::ChocolafApp app(argc, argv);
   app.setStyle("Chocolaf");

   // create the GUI
   DrawWindow mainWindow;
   mainWindow.resize(QGuiApplication::primaryScreen()->availableSize() * 4 / 5);
   mainWindow.show();

   return app.exec();
}
