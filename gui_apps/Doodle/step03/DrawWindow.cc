// DrawWindow.cc: implements DrawWindow class
#include <QMessageBox>
#include <QtGui>
#include "DrawWindow.h"

DrawWindow::DrawWindow()
{
  setAttribute(Qt::WA_StaticContents);
  // setWindowTitle(WinTitle);
  // resize(640,480);
  _modified = false;
}

void DrawWindow::closeEvent(QCloseEvent *event)
{
  // window is about to close, prompt user & decide
  // if ok to quit based on user's response.
  if (_modified) {
    switch (QMessageBox::question(
        this, tr("Qt Scribble Tutorial"),
        tr("This will close the application.\nOk to quit now?"),
        QMessageBox::Yes | QMessageBox::No, QMessageBox::No)) {
    case QMessageBox::Yes:
      // ok to quit
      event->accept();
      break;
    default:
      // don't quit yet
      event->ignore();
    }
  }
  else {
    event->accept();
  }
}

void DrawWindow::drawPoint(const QPoint &pt)
{
  // display position where the mouse was clicked
  QString str;
  QTextStream ostr(&str); // like a string stream

  ostr << "(" << pt.x() << ", " << pt.y() << ")";

  QPainter painter(&_image);
  QFont font("Monospace", 10);
  painter.setFont(font);
  painter.drawText(pt.x(), pt.y(), str);
  update();
}

void DrawWindow::clearImage()
{
  _image.fill(qRgb(255, 255, 255));
  update();
}

void DrawWindow::mousePressEvent(QMouseEvent *event)
{
  // if user clicks the left mouse button, then display position
  // where mouse was clicked. If right button pressed, clear the
  // entire drawing canvas
  if (event->button() == Qt::LeftButton) {
    drawPoint(QPoint(event->pos().x(), event->pos().y()));
    _modified = true;
  } else if (event->button() == Qt::RightButton) {
    clearImage();
    _modified = false;
  }
}

void DrawWindow::resizeEvent(QResizeEvent *event) {
  /*
  qDebug() << "resizeEvent(): width = " << width() << " height() = "
    << height() << " _image.width() = " << _image.width()
    << " _image.height() = " << _image.height();
  */

  if (width() > _image.width() || height() > _image.height()) {
    // need to expand image
    int newWidth = qMax(width(), _image.width());
    int newHeight = qMax(height(), _image.height());
    resizeImage(QSize(newWidth, newHeight));
    update();
  }
  QWidget::resizeEvent(event);
}

void DrawWindow::paintEvent(QPaintEvent *event)
{
  QPainter painter(this);
  QRect dirtyRect = event->rect();
  painter.drawImage(dirtyRect, _image, dirtyRect);
}

void DrawWindow::resizeImage(const QSize &newSize)
{
  if (_image.size() == newSize)
    return;
  // create a  new image matching the new size
  QImage newImage(newSize, QImage::Format_RGB32);
  newImage.fill(qRgb(255, 255, 255));

  // draw existing image over new image & mark it as new image
  QPainter painter(&newImage);
  painter.drawImage(QPoint(0, 0), _image);
  _image = newImage;
}
