#include "mainwindow.h"
#include "common_funcs.h"
#include "ui_mainwindow.h"
#include <QObject>

MainWindow::MainWindow(PaletteSwitcher *ps, QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow), _ps(ps)
{
   Q_ASSERT(ps != nullptr);
   ui->setupUi(this);
   ui->slider->setValue(25);
   QString ver = QString("Built with Qt %1").arg(QT_VERSION_STR);
   ui->qtVer->setText(ver);
   connect(ui->pushButton2, &QPushButton::clicked, this, switchPalette);
   this->_timerId = this->startTimer(1000);
}

MainWindow::~MainWindow() { delete ui; }

void MainWindow::switchPalette()
{
   Q_ASSERT(_ps != nullptr);
   _ps->swapPalettes();
}

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