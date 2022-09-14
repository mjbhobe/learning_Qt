#include <cstdlib>
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);

int main(int argc, char **argv)
{
   QCoreApplication app(argc, argv);

   cout << "Hello World! Welcome to Qt " << QT_VERSION_STR 
      << ". A better way to do C++." << Qt::endl;
   return EXIT_SUCCESS;
}
