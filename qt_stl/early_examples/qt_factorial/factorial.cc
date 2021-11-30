// factorial.cc - computes factorials
#include "gmpxx.h" // GNU multi-precision C++
#include <QTextStream>
#include <cstdio>
#include <cstdlib>
// NOTE: DO NOT include <iostream>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

using namespace std;

int main(void)
{
   long factArg{0};

   do {
      ::fflush(stdin);
      cout << "Factorial of (enter -ve num to quit): " << Qt::flush;
      cin >> factArg;
      if (factArg < 0)
         break;
      mpz_class fact = mpz_class::factorial(factArg);
      cout << factArg << "! = " << fact.get_str().c_str() << Qt::endl;
   } while (true); // infinite loop

   return EXIT_SUCCESS;
}
