// HelloWorld/main.cc
#include "common_funcs.h"
#include <QApplication>
#include <QLabel>
#include <QVBoxLayout>
#include <QWidget>

int main(int argc, char **argv)
{
  QApplication app(argc, argv);
  app.setFont(QApplication::font("QMenu"));
  app.setStyle("Fusion");
  //PaletteSwitcher palSwitcher(&app);

  QWidget win;
  ThemeSwitcher::setDarkTheme(&win);
  win.setWindowTitle("Hello World!");
  QString text = QString("Hello World! Welcome to programming with Qt %1").arg(QT_VERSION_STR);
  QLabel *hello = new QLabel(text);
  QVBoxLayout *main = new QVBoxLayout;
  main->addWidget(hello);
  win.setLayout(main);
  win.show();

  return app.exec();
}
