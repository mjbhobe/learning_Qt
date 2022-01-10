#ifndef IMAGEEDITOR_H
#define IMAGEEDITOR_H

#include <QDir>
#include <QFileDialog>
#include <QMainWindow>
#include <QStringList>
class QLabel;
class QScrollArea;
class QScrollBar;
class QAction;
class QFileDialog;

QT_BEGIN_NAMESPACE
namespace Ui {
class ImageEditor;
}
QT_END_NAMESPACE

class ImageSpinner;

class ImageEditor : public QMainWindow
{
   Q_OBJECT

 public:
   ImageEditor(QWidget *parent = nullptr);
   ~ImageEditor();

   bool loadImage(const QString &imagePath);
   void initializeFileDialog(QFileDialog &dialog, QFileDialog::AcceptMode acceptMode);

 private slots:
   void open();
   void print();
   
   void blurImage();

   void zoomIn();
   void zoomOut();
   void normalSize();
   void fitToWindow();
   void prevImage();
   void nextImage();

   void about();

 private:
   void createActions();
   void createMenus();
   void createToolbars();
   void updateActions();
   void scaleImage(double factor);
   void adjustScrollBar(QScrollBar *scrollBar, double factor);

   QImage *image;
   ImageSpinner *imageSpinner;
   bool imageLoaded;
   QLabel *imageLabel;
   QScrollArea *scrollArea;
   double scaleFactor;

   // actions
   QAction *openAction;
   QAction *printAction;
   QAction *blurAction;
   QAction *exitAction;
   QAction *zoomInAction;
   QAction *zoomOutAction;
   QAction *zoomNormalAction;
   QAction *fitToWindowAction;
   QAction *nextImageAction;
   QAction *prevImageAction;
   QAction *aboutAction;
   QAction *aboutQtAction;
};

class ImageSpinner : public QObject
{
 public:
   ImageSpinner(const QString &imagePath);
   QString nextImage();
   QString prevImage();
   bool atFirst() const;
   bool atLast() const;

 protected:
   int m_currIndex;
   QDir m_dir;
   QStringList m_fileNames;
};

#endif // IMAGEEDITOR_H
