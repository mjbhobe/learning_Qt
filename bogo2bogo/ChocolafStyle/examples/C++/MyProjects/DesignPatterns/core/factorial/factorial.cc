// factorial.cc - calculate factorial for any number
#include <cstdlib>
#include <gmp.h>
#include <gmpxx.h>
#include <QtCore>
#include "common_funcs.h"

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(int argc, char **argv)
{
   QCoreApplication app(argc, argv);
   long num;
   cout << "Factorial of? " << Qt::flush;
   cin >> num;
   cout << num << "! = " << mpz_class::factorial(num) << Qt::endl;

   return EXIT_SUCCESS;
}
