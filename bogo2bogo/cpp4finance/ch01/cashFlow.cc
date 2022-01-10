// cashFlow.cc - test CashFlowCalculator class
//
#include <iostream>
#include "cashFlowCalc.h"
using namespace std;

int main(int argc, char **argv)
{
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " interest_rate" << endl;
    return -1;
  }

  double rate = atof(argv[1]);
  CashFlowCalculator cfc(rate);
  cout.precision(2);

  cout << "Enter period & cash flow separated by space. -1 to finish" << endl;
  do {
    int period;
    cin >> period;
    if (period == -1)
      break;
    double value;
    cin >> value;
    cfc.addCashPayment(value, period);
  } while(true);

  double pv = cfc.presentValue();
  cout << "The present value is " << fixed << pv << endl;
  return 0;
}

