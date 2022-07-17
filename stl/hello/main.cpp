#ifdef _WIN32
#include <tchar.h>
#else
typedef char _TCHAR;
#define _tmain main
#endif

#include <cmath>
#include <fmt/core.h>
#include <iostream>
#include <stdio.h>
#include <string>
#include <utility>

using namespace std;

void pressAnyKeyToContinue()
{
   fflush(stdin);
   cout << endl << "Press any key to continue...";
   string dummy;
   getline(cin, dummy);
}

int main(int, char **)
{
   string name{""};
   fflush(stdin);
   cout << "Enter name: ";
   getline(cin, name);

   name = (name.length() == 0) ? "World" : name;
   //cout << "Hello " << name << ". Welcome to C++!" << endl;
   cout << fmt::format("Hello {}. Welcome to C++!\n", name);

   auto radius{0.0};
   auto M_PI = std::numbers::pi;
   fflush(stdin);
   cout << "Enter radius: ";
   cin >> radius;
   cout << fmt::format("Circle of radius {:.2f}: area = {:.3f} - circumference {:.3f}\n",
                       radius, M_PI * radius * radius, 2 * M_PI * radius);

   // C++20 allows  you to safely compare integars of different types
   // use cmp_less from #include <utility> in C++20
   int x{-3};
   unsigned int y{7};
   cout << fmt::format("{0} < {1} == {2} cmp_less({3})\n", x, y, (x < y), cmp_less(x, y));

   /* cout printf("Circle of radius %.2f: area = %.3f - circumference = %.3f", radius,
               M_PI * radius * radius, 2 * M_PI * radius); */

   // pressAnyKeyToContinue();

   return 0;
}
