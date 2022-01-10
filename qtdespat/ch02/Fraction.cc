// Fraction.cc - Fraction implementation
#include <QObject>
#include <QString>
#include <QTextStream>
#include <algorithm> // STL algorithm for __gcd()
#include <ostream>
#include "Fraction.h"

Fraction::Fraction(const Fraction& other)
{
  // copy constructor
  if (this != &other) {
    // avoid self copy
    this->m_num = other.m_num;
    this->m_denom = other.m_denom;
  }
}

Fraction& Fraction::operator = (const Fraction& other)
{
  if (this != &other) {
    // don't assign to self!
    this->m_num = other.m_num;
    this->m_denom = other.m_denom;
  }
  return *this;
}

// helper function
void Fraction::__reduce(int& num, int& denom) const
{
  int d = std::__gcd(num, denom);
  num /= d;
  denom /= d;
}

// operations
Fraction Fraction::inverse() const
{
  Fraction f = Fraction(m_denom, m_num);
  return f;
}

Fraction Fraction::add(const Fraction& other) const
{
  int num = (this->m_num * other.denom()) + (this->m_denom * other.num());
  int denom = (this->m_denom * other.denom());
  __reduce(num, denom);
  return Fraction(num, denom);
}

Fraction Fraction::subtract(const Fraction& other) const
{
  int num = (this->m_num * other.denom()) - (this->m_denom * other.num());
  int denom = (this->m_denom * other.denom());
  __reduce(num, denom);
  return Fraction(num, denom);
}

Fraction Fraction::multiply(const Fraction& other) const
{
  int num = (this->m_num * other.denom()) * (this->m_denom * other.num());
  int denom = (this->m_denom * other.denom());
  __reduce(num, denom);
  return Fraction(num, denom);
}

Fraction Fraction::divide(const Fraction& other) const
{
  Fraction o2 = other.inverse();
  Fraction ret = this->multiply(o2);
  return ret;
}

Fraction Fraction::reduce() const
{
  int num = m_num;
  int denom = m_denom;
  __reduce(num, denom);
  return Fraction(num, denom);
}

QString Fraction::toString() const 
{
  QString str = QString("%1/%2").arg(m_num).arg(m_denom);
  return str;
}

//friend 
std::wostream &operator<<(std::wostream &ofs, const Fraction &f) 
{
  ofs << f.toString().toStdWString();
  return ofs;
}

//friend 
QTextStream &operator<<(QTextStream &ofs, const Fraction &f) 
{
  ofs << f.toString();
  return ofs;
}

// friend
Fraction operator + (const Fraction& left, const Fraction& right)
{
  Fraction ret = left;
  ret = ret.add(right);
  return ret;
}

// friend
Fraction operator - (const Fraction& left, const Fraction& right)
{
  Fraction ret = left;
  ret = ret.subtract(right);
  return ret;
}

// friend
Fraction operator * (const Fraction& left, const Fraction& right)
{
  Fraction ret = left;
  ret = ret.multiply(right);
  return ret;
}

// friend
Fraction operator / (const Fraction& left, const Fraction& right)
{
  Fraction ret = left;
  ret = ret.divide(right);
  return ret;
}
