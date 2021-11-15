#ifndef __common_funcs_h__
#define __common_funcs_h__

#include <QtCore>
#include <QtGui>
#include <QtWidgets>

#ifdef Q_OS_WINDOWS
// some common functions
bool windowsDarkThemeAvailable();
bool windowsIsInDarkTheme();
void setWinDarkPalette(QApplication *app);
#endif // Q_OS_WINDOWS

#endif  // __common_funcs_h__
