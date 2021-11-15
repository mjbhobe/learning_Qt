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

  if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
    setWinDarkPalette(&a);

  ImageViewer w;
  w.setFont(QApplication::font("QMenu"));
  w.show();

  return a.exec();
}
