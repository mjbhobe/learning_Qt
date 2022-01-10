// qtio-demo.cc - demonstrate IO with various Qt classes
#include <QtCore> // all Qt core classes

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(void)
{
  cout << "Hello Qt World!" << Qt::endl;
  QDate d1(QDate::currentDate());      // initialize with today's date
  QDate bday(1969,6,22);

  cout << d1.toString() << " - "                  // display in std format (Sat Dec 11 2021)
    << d1.toString("dd-MMM-yyyy") << " - "      // use custom format (11-Dec-2021)
    << Qt::endl;
  cout << "I was born on " << bday.toString("dd-MMM-yyyy") 
    << ". I am approximately " << d1.year() - bday.year() << " years old!" << Qt::endl;

   

  return 0;
}



