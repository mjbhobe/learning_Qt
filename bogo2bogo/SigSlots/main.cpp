#include "common_funcs.h"
#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
   QApplication a(argc, argv);
   a.setFont(QApplication::font("QMenu"));
   a.setStyle("Fusion");

   //#ifdef Q_OS_WINDOWS
   PaletteSwitcher palSwitcher(&a);
   if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
      // setWinDarkPalette(&a);
      palSwitcher.setDarkPalette();
   //#endif

   MainWindow w(&palSwitcher);
   w.setFont(QApplication::font("QMenu"));
   w.show();

   return a.exec();
}
