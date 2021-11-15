#ifndef IMAGEVIEWER_H
#define IMAGEVIEWER_H

#include <QFileDialog>
#include <QMainWindow>
class QLabel;
class QScrollArea;
class QScrollBar;
class QAction;
class QFileDialog;

QT_BEGIN_NAMESPACE
namespace Ui {
class ImageViewer;
}
QT_END_NAMESPACE

class ImageViewer : public QMainWindow
{
  Q_OBJECT

public:
  ImageViewer(QWidget *parent = nullptr);
  ~ImageViewer();

  bool loadImage(const QString &imagePath);
  void initializeFileDialog(QFileDialog &dialog, QFileDialog::AcceptMode acceptMode);

private slots:
  void open();
  void print();
  void zoomIn();
  void zoomOut();
  void normalSize();
  void fitToWindow();
  void about();

private:
  void createActions();
  void createMenus();
  void createToolbar();
  void updateActions();
  void scaleImage(double factor);
  void adjustScrollBar(QScrollBar *scrollBar, double factor);

  QImage *image;
  bool imageLoaded;
  QLabel *imageLabel;
  QScrollArea *scrollArea;
  double scaleFactor;

  // actions
  QAction *openAction;
  QAction *printAction;
  QAction *exitAction;
  QAction *zoomInAction;
  QAction *zoomOutAction;
  QAction *zoomNormalAction;
  QAction *fitToWindowAction;
  QAction *aboutAction;
  QAction *aboutQtAction;
};
#endif // IMAGEVIEWER_H
