#include "MainWindow.h"

#include "common_funcs.h"
#include <QApplication>
#include <QFont>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  QFont font = QFont("SF UI Text", QApplication::font("QMenu").pointSize());
  //a.setFont(QApplication::font("QMenu"));
  a.setFont(font);
  a.setStyle("Fusion");

#ifdef Q_OS_WINDOWS
  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&a);
#endif

  MainWindow w;
  w.setFont(QFont(font.family(), font.pointSize() - 1));
  w.show();

  return a.exec();
}
