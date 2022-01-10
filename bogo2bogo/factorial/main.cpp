#include "common_funcs.h"
#include "widget.h"

#include <QApplication>
#include <gmpxx.h>

int main(int argc, char *argv[])
{
   QApplication app(argc, argv);
   app.setFont(QApplication::font("QMenu"));
   app.setStyle("Fusion");
   //PaletteSwitcher palSwitcher(&app);

   /*
   //#ifdef Q_OS_WINDOWS
   if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
      palSwitcher.setDarkPalette();
   //#endif
   */

   Widget w;
   ThemeSwitcher::setDarkTheme(&w);
   w.show();

   return app.exec();
}
