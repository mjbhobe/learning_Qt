#include "ImageViewer.h"

#include "common_funcs.h"
#include <QtCore>
#include <QtGui>
#include <QtWidgets>

int main(int argc, char *argv[])
{
   QApplication app(argc, argv);
   app.setFont(QApplication::font("QMenu"));
   app.setStyle("Fusion");
   PaletteSwitcher palSwitcher(&app);

   //#ifdef Q_OS_WINDOWS
   if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
      palSwitcher.setDarkPalette();
   //#endif

   ImageViewer w;
   w.setFont(QApplication::font("QMenu"));
   w.show();

   return app.exec();
}
