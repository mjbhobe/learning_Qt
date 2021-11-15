// common.hxx : helper function declarations
#ifndef __common_hxx__
#define __common_hxx__

#include <QTextStream>
//#include <gmpxx.h> // GNU arbit precision numbers

QTextStream &operator<<(QTextStream &ost, const mpz_class &c);

#endif // __common_hxx__
