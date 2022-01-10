// complex.cc - implemenation of Complex class
#include <QObject>
#include <QTextStream>
#include <cmath>
#include "Complex.h"

Complex::Complex(const Complex& other)
{
  // copy constructor
  if (this != &other) {
    m_re = other.m_re;
    m_im = other.m_im;
  }
}

Complex& Complex::operator = (const Complex& other)
{
  if (this != &other) {
    m_re = other.m_re;
    m_im = other.m_im;
  }
  return *this;
}

double Complex::norm() const
{
  // norm(a + jb) = (a**2 + b**2)
  return pow(m_re,2) + pow(m_im, 2);
}

double Complex::abs() const
{
  // abs = sqrt(norm())
  return sqrt(norm());
}

double Complex::arg() const
{
  return std::atan2(this->imag(), this->real());
}

// friend
Complex operator + (const Complex& c1, const Complex& c2)
{
  // (a + jb) + (c + jd) = (a + c) + j(b + d)
  Complex ret = {c1.m_re + c2.m_re, c1.m_im + c2.m_im};
  return ret;
}

// friend
Complex operator - (const Complex& c1, const Complex& c2)
{
  // (a + jb) - (c + jd) = (a - c) + j(b - d)
  Complex ret = {c1.m_re - c2.m_re, c1.m_im - c2.m_im};
  return ret;
}

// friend
Complex operator * (const Complex& c1, const Complex& c2)
{
  // (a + jb) * (c + jd) = (ac - bd) + j(bc + ad)
  Complex ret = {c1.m_re * c2.m_re - c1.m_im * c2.m_im,
                 c1.m_im * c2.m_re + c1.m_re * c2.m_im};
  return ret;
}

// friend
Complex operator / (const Complex& c1, const Complex& c2)
{
  // (a + jb) / (c + jd) = (ac + bd)/(c**2 + d**2) + j(bc - ad)/(c**2 + d**2)
  double conj = pow(c2.m_re,2) + pow(c1.m_im,2);
  Complex ret = {(c1.m_re * c2.m_re + c1.m_im * c2.m_im) / conj,
                 (c1.m_im * c2.m_re - c1.m_re * c2.m_im) / conj};
  return ret;
}

// friend
QTextStream& operator << (QTextStream& ost, const Complex& c)
{
  ost << c.m_re << (c.m_im < 0 ? " - " : " + ")
    << qAbs(c.m_im) << "j";
  return ost;
}

