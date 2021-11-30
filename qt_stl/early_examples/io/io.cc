// io.cc - IO functions in Qt/C++
#include "gmpxx.h" // GNU multi-precision C++
#include <QDate>
#include <QString>
#include <QTextStream>
#include <cstdio>
#include <cstdlib>
// NOTE: DO NOT include <iostream>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

using namespace std;

int main(void)
{
   QDate today = QDate::currentDate();
   QString yourName;
   int birthYear;

   ::fflush(stdin);
   cout << "What's your name? " << Qt::flush;
   yourName = cin.readLine();
   cout << "What year were you born? " << Qt::flush;
   cin >> birthYear;

   cout << "Hi " << yourName << "! You are approximately " << (today.year() - birthYear) << " years old today. "
        << Qt::endl;

   return EXIT_SUCCESS;
}
