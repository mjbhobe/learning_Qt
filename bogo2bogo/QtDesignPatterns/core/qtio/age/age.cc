// age.cc - age calculator
#include <QtCore>
#include <cstdlib>
#include <fmt/core.h>
#include <string>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

QDate readBday()
{
   while (true) {
      cout << "Enter your birthday (dd/mm/yyyy) format (e.g. 22/04/1976): " << Qt::flush;
      QString bday = cin.readLine();
      QStringList comps = bday.split("/");
      bool ok;
      int day = comps.at(0).toInt(&ok);
      int mth = comps.at(1).toInt(&ok);
      int year = comps.at(2).toInt(&ok);
      year = (year < 1000) ? 1900 + year : year;
      qDebug() << "day: " << day << " - mth: " << mth << "- year: " << year;
      QDate bdate(year, mth, day);
      if (bdate.isValid()) {
         return bdate;
      } else {
         cerr << "FATAL: incorrect format for birthday!" << Qt::endl;
         continue;
      }
   }
   return QDate::currentDate();
}

int main(void)
{
   QDate birthdate = readBday();
   qDebug() << fmt::format("You were born on {}", birthdate.toString("dd-MMM-yy")).c_str()
            << Qt::flush;
   QDate today = QDate::currentDate();
   qDebug() << "Today is " << today.toString() << Qt::flush;
   const int DAYS_PER_YEAR = 365;
   cout << "You are approximately " << int(birthdate.daysTo(today) / DAYS_PER_YEAR)
        << " years old" << Qt::endl;
   return EXIT_SUCCESS;
}
