#include "Textfinder.h"
#include "common_funcs.h"

#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  QFont font = QFont("SF UI Text", QApplication::font("QMenu").pointSize());
  app.setFont(QApplication::font("QMenu"));
  app.setStyle("Fusion");

/*#ifdef Q_OS_WINDOWS
  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&app);
#endif
*/

  TextFinder w;
  ThemeSwitcher::setDarkTheme(&w);
  w.setFont(font);
  w.show();

  return app.exec();
}
