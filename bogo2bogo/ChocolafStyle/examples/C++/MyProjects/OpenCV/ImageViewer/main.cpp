#include <QtCore>
#include <QtGui>
#include <QtWidgets>

#include "ImageViewer.h"
#include "common_funcs.h"
#include "chocolaf.h"

int main(int argc, char *argv[])
{
   Chocolaf::ChocolafApp app(argc, argv);
   //app.setFont(QApplication::font("QMenu"));
   app.setStyle("Chocolaf");

   ImageViewer w;
/*
#ifdef Q_OS_WINDOWS
   if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
      winDark::ThemeSwitcher::setDarkTheme(&w);
#else
   winDark::ThemeSwitcher::setDarkTheme(&w);
#endif
   w.setFont(QApplication::font("QMenu"));
*/
   w.show();

   return app.exec();
}
