// interestCalculator.cc - simple/compound interest calculators
//
#include <iostream>
#include "interestCalc.h"

InterestCalculator::InterestCalculator(double rate)
  : m_rate(rate)
{
  // done!
}

InterestCalculator::~InterestCalculator()
{
  // nothing more
}

InterestCalculator::InterestCalculator(const InterestCalculator &o)
  : m_rate(o.m_rate)
{
  // done!
}

InterestCalculator& InterestCalculator::operator = (const InterestCalculator &o)
{
  if (this != &o) {
    m_rate = o.m_rate;
  }
  return *this;
}


