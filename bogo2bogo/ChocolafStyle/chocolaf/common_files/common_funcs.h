#ifndef __common_funcs_h__
#define __common_funcs_h__

#pragma GCC diagnostic ignored "-Wc++17-attribute-extensions"

#include <QTextStream>
#include <QtCore>

#ifndef _MSC_VER
#include <gmpxx.h> // GNU arbit precision numbers
QTextStream &operator<<(QTextStream &ost, const mpz_class &c);
#endif

bool windowsDarkThemeAvailable();
bool windowsIsInDarkTheme();

#endif // __common_funcs_h__
