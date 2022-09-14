// qtio.cc - I/O with Qt and C++
#include <cstdlib>
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(int argc, char **argv)
{
   QCoreApplication app(argc, argv);
   QDate today = QDate::currentDate();

   cout << "What's your name? " << Qt::flush;
   QString name = cin.readLine();
   cout << "In which year were you born? " << Qt::flush;
   int year;
   cin >> year;
   cout << "Hello " << name << ". Next year you will be approx. " << (today.year() - year + 1)
      << " years old" << Qt::endl;

   return EXIT_SUCCESS;
}
