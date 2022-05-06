// ============================================================================
// step08.cc: Adding toolbar & status bar
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================

#include "MainWindow.h"
#include "common.hxx"
#include <QApplication>
#include <QDebug>
#include <QStyleFactory>
#include <QtGui>

static MainWindow *__pMainWindow = nullptr;
MainWindow *getMainWindow()
{
   // it is assumed that this will always be a  valid ptr
   // from all points where it is called from. Hence the assert
   Q_ASSERT(__pMainWindow != nullptr);
   return __pMainWindow;
}

int main(int argc, char **argv)
{
   QApplication app(argc, argv);
   // QApplication::setStyle(QStyleFactory::create("Fusion"));
   app.setStyle("Fusion");

#ifdef Q_OS_WINDOWS
   if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
      setWinDarkPalette(&app);
#endif

   // create the GUI
   MainWindow *mainWindow = new MainWindow();
   __pMainWindow = mainWindow;
   mainWindow->show();

   int ret = app.exec();
   delete mainWindow;
   return ret;
}
