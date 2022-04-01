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
#include "chocolaf.h"

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

