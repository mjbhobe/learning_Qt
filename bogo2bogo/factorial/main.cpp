#include "common_funcs.h"
#include "widget.h"

#include <gmpxx.h>
#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  app.setFont(QApplication::font("QMenu"));
  app.setStyle("Fusion");

#ifdef Q_OS_WINDOWS
  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&app);
#endif

  Widget w;
  w.show();

  return app.exec();
}
