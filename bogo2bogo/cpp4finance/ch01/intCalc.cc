#include <iostream>
#include "interestCalc.h"
using namespace std;

int main(int argc, char **argv)
{
  // set floating point precision to 4 digits
  cout.precision(2);

  // expecting 3 args: progname int_rate principle
  if (argc != 4) {
    cerr << "Usage: " << argv[0] << " interest_rate principle periods" << endl;
    return -1;
  }

  double rate = atof(argv[1]);
  double principle = atof(argv[2]);
  int periods = atoi(argv[3]);

  InterestCalculator calc(rate);
  cout << "Interest rate calculator - principle = " << principle 
    << " rate = " << rate << " periods = " << periods << endl;
  cout << "   Simple Interest        : " << fixed 
    << calc.simpleInterest(principle, periods) << endl;
  cout << "   Compound Interest      : " << fixed
    << calc.compoundInterest(principle, periods) << endl;
  cout << "   Continuous Compounding : " << fixed
    << calc.contCompoundInterest(principle, periods) << endl;
  return 0;
}



    
