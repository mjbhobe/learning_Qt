// ============================================================================
// step02.cc: Handling events in the main window with Qt's signals/slots
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
//
// @author Manish Bhobe for Nämostuté Ltd.
// My experiments with C++,Qt, Python & PyQt.
// Code is provided for illustration purposes only! Use at your own risk.
// =============================================================================

#include <QApplication>
#include <QtGui>
#include "chocolaf.h"
#include "DrawWindow.h"

int main(int argc, char **argv)
{
   Chocolaf::ChocolafApp app(argc, argv);
   app.setStyle("Chocolaf");
   app.setApplicationName(app.translate("main", "Qt Scribble"));

   // create the GUI
   DrawWindow mainWindow;
   mainWindow.show();

   return app.exec();
}
