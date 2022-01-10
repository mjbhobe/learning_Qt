#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "common_funcs.h"
#include <QMainWindow>

class QTimerEvent;

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
   Q_OBJECT

 public:
   MainWindow(QWidget *parent = nullptr);
   ~MainWindow();

 private:
   Ui::MainWindow *ui;
   bool usingDarkPalette;

 private slots:
   void switchPalette();
};
#endif // MAINWINDOW_H
