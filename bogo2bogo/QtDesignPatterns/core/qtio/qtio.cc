// qtio.cc - illustrates input/output
#include <QtCore>
#include <cstdlib>
#include <fmt/core.h>
#include <string>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int promptInt(const char *msg = nullptr)
{
   if (msg)
      cout << msg << Qt::flush;
   fflush(stdin);
   int ret;
   cin >> ret;
   return ret;
}

int main(void)
{
   std::string s = fmt::format("Hello {}", "World!");
   cout << s.c_str() << Qt::endl;

   QDate d1(2022, 1, 1), d2(QDate::currentDate());

   cout << "First date is " << d1.toString("dd-MMM-yy")
        << " - today's date: " << d2.toString("dd-MMM-yy") << Qt::endl;
   cout << "There are " << d1.daysTo(d2) << " days between them" << Qt::endl;

   int value = promptInt("Enter no of days to add: ");
   cout << "Adding " << value << " days to " << d1.toString("dd-MMM-yy") << " gives me "
        << d1.addDays(value).toString("dd-MMM-yy") << Qt::endl;

   return EXIT_SUCCESS;
}
