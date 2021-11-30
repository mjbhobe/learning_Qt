#include "MainWindow.h"
#include "common_funcs.h"

#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  app.setStyle("Fusion");
  PaletteSwitcher ps(&app);

  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    ps.setDarkPalette();

  MainWindow w;
  w.show();

  return app.exec();
}
