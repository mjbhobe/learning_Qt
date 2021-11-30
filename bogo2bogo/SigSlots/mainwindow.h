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
   MainWindow(PaletteSwitcher *ps, QWidget *parent = nullptr);
   ~MainWindow();

 private:
   Ui::MainWindow *ui;
   PaletteSwitcher *_ps;
   int _timerId;
   void timerEvent(QTimerEvent *event);

 private slots:
   void switchPalette();
};
#endif // MAINWINDOW_H
