// ============================================================================
// step03.cc: Drawing in the main window
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// ===========================================================================
#include "DrawWindow.h"
#include "common.hxx"
#include <QApplication>
#include <QMainWindow>
#include <QMessageBox>
#include <QtGui>

const QString AppTitle("Qt Scribble");
const QString WinTitle("Qt Doodle - Step03: Handling mouse clicks");

void DrawMainWindow::closeEvent(QCloseEvent *event)
{
   // window is about to close, prompt user & decide
   // if ok to quit based on user's response.
   qDebug() << "DrawMainWindow::closeEvent() called. _modified = "
            << (_drawWindow->isModified() ? "True" : "False");

   if (_drawWindow->isModified()) {
      switch (
         QMessageBox::question(this, tr("Qt Scribble Tutorial"),
                               tr("Contents of the doodle have changed.\nDo you want to quit without saving?"),
                               QMessageBox::Yes | QMessageBox::No, QMessageBox::No)) {
         case QMessageBox::Yes:
            // ok to quit
            qDebug() << "User chose to quit without saving...";
            event->accept();
            break;
         default:
            // don't quit yet
            event->ignore();
      }
   } else {
      event->accept();
   }
}

int main(int argc, char **argv)
{
   QApplication app(argc, argv);
   app.setFont(QApplication::font("QMenu"));
   app.setStyle("Fusion");

#ifdef Q_OS_WINDOWS
   if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
     setWinDarkPalette(&app);
#endif

   // create the GUI
   DrawWindow *drawWidget = new DrawWindow;
   DrawMainWindow mainWindow(drawWidget);
   mainWindow.setWindowTitle(WinTitle);
   mainWindow.setCentralWidget(drawWidget);
   mainWindow.resize(QGuiApplication::primaryScreen()->availableSize() * 4 / 5);
   mainWindow.show();

   return app.exec();
}

