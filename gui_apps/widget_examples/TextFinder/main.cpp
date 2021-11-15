#include "Textfinder.h"

#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  TextFinder w;
  w.setFont(QApplication::font("QMenu"));
  w.show();
  return a.exec();
}
