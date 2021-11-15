#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
  : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
  ui->setupUi(this);
  ui->slider->setValue(25);
  QString ver = QString("Built with Qt %1").arg(QT_VERSION_STR);
  ui->qtVer->setText(ver);
}

MainWindow::~MainWindow()
{
  delete ui;
}

