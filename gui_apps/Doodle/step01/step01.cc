// ============================================================================
// step01.cc: Creating a basic application
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// My experiments with the Qt Framework. Use at your own risk!!
// ============================================================================

#include <QApplication>
#include <QMainWindow>
#include <QtGui>

int main(int argc, char **argv)
{
   QApplication app(argc, argv);

   // create the GUI
   QMainWindow mainWindow;
   mainWindow.setWindowTitle("Qt Scribble Tutorial - Step01");
   mainWindow.setStyleSheet("background-color: white;");
   mainWindow.resize(640, 480);
   mainWindow.show();

   return app.exec();
}
