#include <QApplication>
#include "TextFinder.h"

int main(int argc, char **argv)
{
  QApplication app(argc, argv);

  TextFinder textFinder;
  textFinder.show();

  return app.exec();
}
