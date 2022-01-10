// cashFlowCalc.cc - simple/compound interest calculators
//
#include <cmath>
#include <iostream>
#include "cashFlowCalc.h"
using namespace std;

CashFlowCalculator::CashFlowCalculator(double rate)
  : m_rate(rate)
{
  // done!
}

CashFlowCalculator::~CashFlowCalculator()
{
  // nothing more
}

CashFlowCalculator::CashFlowCalculator(const CashFlowCalculator &o)
  : m_rate(o.m_rate)
{
  // done!
}

CashFlowCalculator& CashFlowCalculator::operator = (const CashFlowCalculator &o)
{
  if (this != &o) {
    m_rate = o.m_rate;
    m_cashPayments = o.m_cashPayments;
    m_timePeriods = o.m_timePeriods;
  }
  return *this;
}

void CashFlowCalculator::addCashPayment(double value, int timePeriod)
{
  m_cashPayments.push_back(value);
  m_timePeriods.push_back(timePeriod);
}

double CashFlowCalculator::presentValue(double futureValue, int timePeriod)
{
  // calculate present value of a future payment for a time period
  double pv = futureValue / pow(1 + m_rate, timePeriod);
  cout << " value " << fixed << pv << endl;
  return pv;
}

double CashFlowCalculator::presentValue()
{
  // calculate present value of all payments
  double pv = 0.0;
  for (auto i = 0; i < m_timePeriods.size(); ++i)
    pv += presentValue(m_cashPayments[i], m_timePeriods[i]);
  return pv;
}




