#ifndef __TextFinder_h__
#define __TextFinder_h__

#include "ui_TextFinder.h"
#include <QWidget>

class TextFinder : public QWidget {
  Q_OBJECT
private:
  void loadTextFile();
  Ui::TextFinder *ui;
private slots:
    void onFindButtonClicked();
public:
    TextFinder(QWidget *parent = nullptr);
};

#endif // __TextFinder_h__
