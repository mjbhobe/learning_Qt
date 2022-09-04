// basic.cc - basic Hello World with Qt core module
#include <cstdlib>
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(void)
{
   cout << QString("Hello World! Welcome to Qt %1").arg(QT_VERSION_STR)
      << Qt::endl;
   return EXIT_SUCCESS;
}

