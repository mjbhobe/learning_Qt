#include "mainwindow.h"
#include "dialog.h"
#include "ui_dialog.h"
#include "ui_mainwindow.h"

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
  myDialog.setFont(QApplication::font("QMenu"));
  myDialog.setModal(true);
  myDialog.ui->label->setText("I am a modal dialog");
  myDialog.exec();
}
