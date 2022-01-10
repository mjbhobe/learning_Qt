// main.c
#include <QTextStream>
#include "Fraction.h"

static QTextStream cout(stdout, QIODevice::WriteOnly);

int main(void)
{
  Fraction f0(7);
  cout << "Fraction(7) = " << f0 << Qt::endl;

  Fraction f1(45, 75);
  cout << "Fraction(45, 75) = " << f1 << " - reduced: " 
    << f1.reduce() << " - inverse: " << f1.inverse() 
    << " - inverse reduced: " << f1.inverse().reduce() << Qt::endl;

  Fraction f2 = f1.inverse();
  cout << "Fraction(45,75) + Fraction(75, 45) = " << f1.add(f2) 
    << " - reduced = " << f1.add(f2).reduce() << Qt::endl;

  Fraction f3 = Fraction(125,135) - Fraction(120, 270);
  cout << "Fraction(125,135) - Fraction(120, 270) = " << f3 << Qt::endl;

 


  return 0;
}


