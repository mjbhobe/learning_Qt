#include "common_funcs.h"
#include "mainwindow.h"

#include <QApplication>

PaletteSwitcher *g_palSwitcher = nullptr;

int main(int argc, char *argv[])
{
   QApplication app(argc, argv);
   QFont font("SF UI Text", QApplication::font("QMenu").pointSize());
   app.setFont(font);
   //a.setFont(QApplication::font("QMenu"));
   app.setStyle("Fusion");

   /*
   //#ifdef Q_OS_WINDOWS
   PaletteSwitcher palSwitcher(&a);
   g_palSwitcher = &palSwitcher;
   if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
      // setWinDarkPalette(&a);
      palSwitcher.setDarkPalette();
   //#endif
   */

   MainWindow w;
   ThemeSwitcher::setDarkTheme(&w);
   //w.setFont(QApplication::font("QMenu"));
   w.setFont(font);
   w.show();

   return app.exec();
}
