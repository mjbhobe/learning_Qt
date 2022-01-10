// Fraction.h - define Fraction class
#ifndef __Fraction_h__
#define __Fraction_h__

#include <QObject>
#include <QString>
#include <stdexcept>
#include <ostream>

class QTextStream;

class Fraction : public QObject {   
      Q_OBJECT
   public:
      Fraction(int num)
        : m_num(num), m_denom(1)
      {
        // nothing more...
      }
      Fraction(int num, int denom)
        : m_num(num), m_denom(denom)
      {
        if (m_denom == 0)
          throw std::invalid_argument("Fraction error - denominator cannot be == 0");
      }
      Fraction(const Fraction& f);
      Fraction& operator = (const Fraction& f);
      
      int num() const { return m_num; }
      void setNum(const int& num) { m_num = num; }
      int denom() const { return m_denom; }
      void setDenom(const int& denom) {
        if (denom == 0)
          throw std::invalid_argument("Fraction error - setDenom() - denominator cannot == 0");
        m_denom = denom;
      }

      // operations
      Fraction inverse() const;
      Fraction add(const Fraction& f) const;
      Fraction subtract(const Fraction& f) const;
      Fraction multiply(const Fraction& f) const;
      Fraction divide(const Fraction& f) const;
      Fraction reduce() const;
      QString toString() const;

      // operator overloads
      // f3 = f1 + f2
      friend Fraction operator + (const Fraction& left, const Fraction& right);
      friend Fraction operator - (const Fraction& left, const Fraction& right);
      friend Fraction operator * (const Fraction& left, const Fraction& right);
      friend Fraction operator / (const Fraction& left, const Fraction& right);

      // helpers
      friend std::wostream &operator<<(std::wostream &ofs, const Fraction &f);
      friend QTextStream &operator<<(QTextStream &ofs, const Fraction &f);
    
   private:
      int m_num, m_denom;
      void __reduce(int& num, int& denom) const;
};


#endif   // __Fraction_h__
