// example1.cc - basic QStringList functions
#include <QtCore>
#include <cstdlib>
#include <string>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

QTextStream& operator << (QTextStream& ost, QStringList& lst)
{
   const QString SEP {", "};
   ost << "[" << lst.join(SEP) << "]" << Qt::endl;
   return ost;
}

int main(void)
{
   QString winter {"December, January, February"};
   QString spring {"March, April, May"};
   QString summer {"June, July, August"};
   QString autumn {"September, October, November"};

   QStringList list{};

   // various means of adding values to a stringlist
   list << winter;
   list += spring;
   list.append(summer);
   list << autumn;
   cout << list << Qt::endl;

   return EXIT_SUCCESS;
}

