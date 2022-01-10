// cashFlowCalc.h - simple interest rate calculator

#ifndef __FinSamples_CashFlowCalculator__
#define __FinSamples_CashFlowCalculator__

#include <vector>

class CashFlowCalculator {
  public:
    // construction & destruction
    CashFlowCalculator(double rate);
    CashFlowCalculator(const CashFlowCalculator &o);
    CashFlowCalculator& operator = (const CashFlowCalculator &o);
    ~CashFlowCalculator();

    // methods
    void addCashPayment(double value, int timePeriod);
    double presentValue();

  private:
    double m_rate;
    std::vector<double> m_cashPayments;
    std::vector<int> m_timePeriods;
    double presentValue(double futureValue, int timePeriod);
};

#endif   // __FinSamples_SimpleIntRateCalc__

    
