// DrawWindow.cc: implements DrawWindow class
#include <QtGui>
#include <QMessageBox>
#include "DrawWindow.h"

DrawWindow::DrawWindow()
{
  setWindowTitle("Qt Scribble Application - Step02: Handling events");
  setStyleSheet("background-color: white;");
  resize(640,480);
}

void DrawWindow::closeEvent(QCloseEvent *event)
{
  // window is about to close, prompt user & decide if ok to quit
  // based on user's response.
  switch(QMessageBox::question(this, tr("Qt Scribble Tutorial"),
       tr("This will close the application.\nOk to quit now?"),
       QMessageBox::Yes|QMessageBox::No, QMessageBox::No))
  {
    case QMessageBox::Yes:
      // ok to quit
      event->accept();
      break;
    default:
      // don't quit yet
      event->ignore();
  }
}

void DrawWindow::mousePressEvent(QMouseEvent *event)
{
  if (event->button() == Qt::LeftButton) {
    QMessageBox::information(this, tr("Qt Scribble Tutorial"),
        tr("You have pressed the LEFT mouse button!"));
  }
  else if (event->button() == Qt::RightButton) {
    QMessageBox::information(this, tr("Qt Scribble Tutorial"),
        tr("You have pressed the RIGHT mouse button!"));
  }
}
