#ifndef PREVIEWWINDOW_H
#define PREVIEWWINDOW_H

#include <QWidget>
class QTextEdit;
class QPushButton;

class PreviewWindow : public QWidget
{
  Q_OBJECT

public:
  PreviewWindow(QWidget *parent = nullptr);

  void setWindowFlags(Qt::WindowFlags flags);

private:
  QTextEdit *textEdit;
  QPushButton *closeButton;
};

#endif // PREVIEWWINDOW_H
