// SimpleInt.h - simple interest rate calculator

#ifndef __FinSamples_InterestCalculator__
#define __FinSamples_InterestCalculator__

#include <cmath>

class InterestCalculator {
  public:
    // construction & destruction
    InterestCalculator(double rate);
    InterestCalculator(const InterestCalculator &o);
    InterestCalculator& operator = (const InterestCalculator &o);
    ~InterestCalculator();

    // methods
    double simpleInterest(double principle, int periods=1);
    double compoundInterest(double principle, int periods=1);
    double contCompoundInterest(double principle, int periods=1);

  private:
    double m_rate;
};

inline double InterestCalculator::simpleInterest(double principle, int periods)
{
  // simple interest SI = P*T*r
  // future value = P + SI = P + PTr = P(1 + Tr)
  
  double futureValue = principle * (1 + periods * this->m_rate);
  return futureValue;
}


inline double InterestCalculator::compoundInterest(double principle, int periods)
{
  // discrete compound interest calculation
  // future_value = P * (1 + r)^T
  
  double futureValue = principle * pow(1 + this->m_rate, periods);
  return futureValue;
}

inline double InterestCalculator::contCompoundInterest(double principle, int periods)
{
  // continuous compounding interest calculator
  // future_value = P * e^(r*T)

  double futureValue = principle * exp(this->m_rate * periods);
  return futureValue;
}

#endif   // __FinSamples_SimpleIntRateCalc__

    
