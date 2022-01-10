// complex.h - complex number class
#ifndef __Complex_h__
#define __Complex_h__

#include <QObject>

class QTextStream;

class Complex: public QObject {
      Q_OBJECT
   public:
      // constructors
      Complex(double re, double im)
        : m_re(re), m_im(im) {}
      Complex(const Complex& c);
      Complex& operator = (const Complex& other);

      // attributes
      double real() const { return m_re; }
      double imag() const { return m_im; }

      // if complex no = a + bj
      double norm() const;    // = (a**2 + b**2)
      double abs() const;     // = sqrt(norm)
      // angle between real & imag part
      double arg() const;     // atan2(imag(), real())

      friend Complex operator + (const Complex& c1, const Complex& c2);
      friend Complex operator - (const Complex& c1, const Complex& c2);
      friend Complex operator * (const Complex& c1, const Complex& c2);
      friend Complex operator / (const Complex& c1, const Complex& c2);

      friend QTextStream& operator << (QTextStream& ost, const Complex& c);
    private:
      double m_re, m_im;
};
      

#endif   // __Complex_h__
