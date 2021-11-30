#include "ControllerWidget.h"
#include "common_funcs.h"

#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  app.setFont(QApplication::font("QMenu"));
  app.setStyle("Fusion");
  PaletteSwitcher palSwitcher(&app);

  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    palSwitcher.setDarkPalette();

  ControllerWidget w;
  w.show();

  return app.exec();
}
