// -------------------------------------------------------------------------
// factorial.cc : calculate factorials of numbers
// In this example we make use of GNU MPZ class library
//
// @author: Manish Bhobe
// My experiments with C++ & Qt Framework
// This code is meant for learning & educational purposes only!!
// -------------------------------------------------------------------------
#include <QString>
#include <QTextStream>
#include <cstdlib>
#include <gmpxx.h> // GNU arbit precision numbers
using namespace std;

QTextStream cout(stdout, QIODevice::WriteOnly);
QTextStream cin(stdin, QIODevice::ReadOnly);
QTextStream cerr(stderr, QIODevice::WriteOnly);

QTextStream &operator<<(QTextStream &ost, const mpz_class &c)
{
   QString qstr(c.get_str().c_str());
   ost << qstr;
   return ost;
}

mpz_class factorial(mpz_class &num)
{
   mpz_class ans = 1;

   for (mpz_class l = 2; l <= num; l++)
      ans *= l;
   return ans;
}

int main(void)
{
   mpz_class a;
   string num;

   do {
      cout << "Enter a positive number (Enter to quit!): " << flush;
      QString num = cin.readLine();
      if (num.trimmed().length() == 0)
         break;
      a = num.toStdString();
      cout << a << "! = " << factorial(a) << endl;
   } while (true); // infinite loop: broken if you enter blank string (press Enter)

   return 0;
}
