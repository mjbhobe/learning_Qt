#include "ImageViewer.h"

#include "common_funcs.h"
#include <QtCore>
#include <QtGui>
#include <QtWidgets>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  a.setFont(QApplication::font("QMenu"));
  a.setStyle("Fusion");

#ifdef Q_OS_WINDOWS
  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&a);
#endif

  ImageViewer w;
  w.setFont(QApplication::font("QMenu"));
  w.show();

  return a.exec();
}
