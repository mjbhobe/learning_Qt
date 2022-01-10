#include "mainwindow.h"
#include "dialog.h"
#include "ui_dialog.h"
#include "ui_mainwindow.h"
#include "common_funcs.h"

MainWindow::MainWindow(QWidget *parent)
  : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
  ui->setupUi(this);
}

MainWindow::~MainWindow()
{
  delete ui;
}

void MainWindow::on_actionNewWindow_triggered()
{
  // call the dialog
  Dialog myDialog;
  ThemeSwitcher::setDarkTitlebar(myDialog.winId());
  myDialog.setFont(QApplication::font("QMenu"));
  myDialog.setModal(true);
  myDialog.ui->label->setText("I am a modal dialog");
  myDialog.exec();
}
