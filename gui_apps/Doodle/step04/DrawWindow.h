// DrawWindow.h: the main drawing window
#ifndef __DrawWindow_h__
#define __DrawWindow_h__

#include <QMainWindow>

class QImage;
class QColor;

class DrawWindow : public QMainWindow {
  Q_OBJECT
public:
  DrawWindow();

protected:
  // operating system events
  void closeEvent(QCloseEvent *event);
  void paintEvent(QPaintEvent *event);
  void resizeEvent(QResizeEvent *event);

  // event messages
  void mousePressEvent(QMouseEvent *event);
  void mouseMoveEvent(QMouseEvent *event);
  void mouseReleaseEvent(QMouseEvent *event);

private:
  void drawLineTo(const QPoint &pt);
  void clearImage();
  void resizeImage(const QSize &size);

  QImage _image;
  bool _modified;

  QPoint _lastPt;
  bool _dragging;
  int _penWidth;
  QColor _penColor;
};

#endif // __DrawWindow_h__
