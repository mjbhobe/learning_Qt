// factorial.cc - computes factorials
#include "gmpxx.h" // GNU multi-precision C++
#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main(void)
{
   long factArg{0};

   do {
      ::fflush(stdin);
      cout << "Factorial of (enter -ve num to quit): ";
      cin >> factArg;
      if (factArg < 0)
         break;
      mpz_class fact = mpz_class::factorial(factArg);
      cout << factArg << "! = " << fact.get_str().c_str() << endl;
   } while (true); // infinite loop
   return EXIT_SUCCESS;
}
