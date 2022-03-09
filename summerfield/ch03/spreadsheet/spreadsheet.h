#ifndef __SpreadSheet_h__
#define __SpreadSheet_h__

#include <QWidget>

class Spreadsheet : public QWidget
{
  Q_OBJECT
public:
  Spreadsheet(QObject *parent=nullptr): QObject(parent) {}
  ~Spreadsheet();
};

#endif // __SpreadSheet_h__
