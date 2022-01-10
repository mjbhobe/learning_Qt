#include "gmpxx.h"
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(int argc, char *argv[])
{
  QCoreApplication app(argc, argv);

  cout << "Hello World! Welcome to Qt " << QT_VERSION_STR << Qt::endl;

  return app.exec();
}
