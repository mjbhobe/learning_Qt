// signals_and_slots.cc : illustrating using signals & slots with Qt
#include <QApplication>
#include <QMainWindow>
#include "MainWidget.h"

int main(int argc, char** argv)
{
  QApplication app(argc, argv);

  QMainWindow mainWindow;
  mainWindow.setWindowTitle("Qt Signals & Slots Demo");
  MainWidget *mainWidget = new MainWidget();
  mainWindow.setCentralWidget(mainWidget);
  mainWindow.show();

  return app.exec();
}
