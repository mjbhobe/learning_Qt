// main.cc - driver program
#include <QTextStream>
#include <iostream>
#include <complex>
#include "Complex.h"

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

// NOTE: DO NOT use using namespace std!! Use std::.... when neede
// this will allow you to use Qt & STL smoothly

template <class T>
QTextStream& operator << (QTextStream& ost, const std::complex<T>& c)
{
  ost << std::real(c) << (std::imag(c) < 0 ? " - " : " + ")
    << std::imag(c) << "j";
  return ost;
}

int main(void)
{
  Complex c1 = {2.0, 3.0};
  Complex c2 = {4.0, -5.0};
  std::complex<double> sc1 = {2.0, 3.0};
  std::complex<double> sc2 = {4.0, -5.0};

  cout << "c1 = " << c1 << " c2 = " << c2 << Qt::endl;
  cout << "STL c1 = " << sc1 <<  " c2 = " << sc2 << Qt::endl;
  cout << "norm(c1) = " << c1.norm() << " abs(c1) = " << c1.abs() << " arg(c1) = " << c1.arg() << Qt::endl;
  cout << "STL norm(c1) = " << std::norm(sc1) << " abs(c1) = " << std::abs(sc1) << " arg(c1) = " << std::arg(sc1) << Qt::endl;
  cout << "norm(c2) = " << c2.norm() << " abs(c2) = " << c2.abs() << " arg(c2) = " << c2.arg() << Qt::endl;
  cout << "STL norm(c2) = " << std::norm(sc2) << " abs(c2) = " << std::abs(sc2) << " arg(c2) = " << std::arg(sc2) << Qt::endl;


  /*
  cout << "c1.mod() = " << c1.mod() << " c2.mod() = " 
    << c2.mod() << Qt::endl;
  cout << "c1 + c2 = " << c1 + c2 << Qt::endl;
  cout << "c1 - c2 = " << c1 - c2 << Qt::endl;
  cout << "c1 * c2 = " << c1 * c2 << Qt::endl;
  cout << "c1 / c2 = " << c1 / c2 << Qt::endl;
  cout << "Complex number addition is commutative (c1 + c2 == c2 + c1)" << Qt::endl;
  cout << "c1 + c2 = " << c1 + c2 << " and c2 + c1 = " 
    << c2 + c1 << Qt::endl;
  cout << "Complex number multiplication is commutative (c1 * c2 == c2 * c1)" << Qt::endl;
  cout << "c1 * c2 = " << c1 * c2 << " and c2 * c1 = " 
    << c2 * c1 << Qt::endl;
  */
  return 0;
}

