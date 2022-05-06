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
   QMainWindow mainWindow;
   mainWindow.setWindowTitle("Qt5 Doodle - Step01: Basic Window");
   // mainWindow.setStyleSheet("background-color: white;");
   mainWindow.resize(QGuiApplication::primaryScreen()->availableSize() * 4 / 5);
   mainWindow.show();

   return app.exec();
}
