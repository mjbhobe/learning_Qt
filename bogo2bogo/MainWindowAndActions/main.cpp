#include "common_funcs.h"
#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  a.setFont(QApplication::font("QMenu"));
  a.setStyle("Fusion");

#ifdef Q_OS_WINDOWS
  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&a);
#endif

  MainWindow w;
  w.show();

  return a.exec();
}
