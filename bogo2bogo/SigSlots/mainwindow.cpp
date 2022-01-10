#include "mainwindow.h"
#include "common_funcs.h"
#include "ui_mainwindow.h"
#include <QObject>

MainWindow::MainWindow(QWidget *parent)
   : QMainWindow(parent), ui(new Ui::MainWindow)
{
   ui->setupUi(this);
   ui->slider->setValue(25);
   usingDarkPalette = true;
   ThemeSwitcher::setDarkTheme(this);

   QString ver = QString("Built with Qt %1").arg(QT_VERSION_STR);
   ui->qtVer->setText(ver);
   connect(ui->pushButton2, &QPushButton::clicked, this, &MainWindow::switchPalette);
   ui->pushButton2->setText(usingDarkPalette ? "Light Palette" : "Dark Palette");
   ui->pushButton2->setToolTip(
      QString("Switch to %1 palette").arg(usingDarkPalette ? "light" : "dark"));
}

MainWindow::~MainWindow() { delete ui; }

void MainWindow::switchPalette()
{
   if (usingDarkPalette) {
     ThemeSwitcher::setLightTheme(this);
     usingDarkPalette = false;
   }
   else {
     ThemeSwitcher::setDarkTheme(this);
     usingDarkPalette = true;
   }

   ui->pushButton2->setText(usingDarkPalette ? "Light Palette" : "Dark Palette");
   ui->pushButton2->setToolTip(
      QString("Switch to %1 palette").arg(usingDarkPalette ? "light" : "dark"));
}

/*
void MainWindow::timerEvent(QTimerEvent *e)
{
   if (e->timerId() == this->_timerId) {
      if (windowsDarkThemeAvailable() && windowsIsInDarkTheme()) {
         // Os is using dark palette, but if I am using light palette swap it
         if (!_ps->isDarkPaletteInUse())
            _ps->swapPalettes();
      } else {
         // Os is using light palette, but if I am using dark palette swap it
         if (_ps->isDarkPaletteInUse())
            _ps->swapPalettes();
      }
      // update();
   }
}
*/
