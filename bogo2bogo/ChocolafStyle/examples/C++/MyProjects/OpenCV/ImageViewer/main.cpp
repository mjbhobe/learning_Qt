#include "argparse/argparse.hpp"
#include <QtCore>
#include <QtGui>
#include <QtWidgets>
#include <filesystem>
#include <fmt/core.h>

#include "ImageViewer.h"
#include "common_funcs.h"
namespace fs = std::filesystem;

const QString AppTitle("Qt with OpenCV ImageViewer");

// define expected command line args
// @see: https://github.com/morrisfranken/argparse
struct MyArgs : public argparse::Args {
  // -i | --image <image_path>
  std::string &image_path = kwargs("i,image", "Full path to image file to display.");
};

int main(int argc, char **argv)
{
  QApplication app(argc, argv);

  QFile f(":chocolaf/chocolaf.css");

  if (!f.exists()) {
    printf("Unable to open stylesheet!");
  } else {
    f.open(QFile::ReadOnly | QFile::Text);
    QTextStream ts(&f);
    app.setStyleSheet(ts.readAll());
  }
  app.setApplicationName(app.translate("main", AppTitle.toStdString().c_str()));

  ImageViewer w;
  /*
  #ifdef Q_OS_WINDOWS
     if (windowsDarkThemeAvailable() && windowsIsInDarkTheme())
        winDark::ThemeSwitcher::setDarkTheme(&w);
  #else
     winDark::ThemeSwitcher::setDarkTheme(&w);
  #endif
     w.setFont(QApplication::font("QMenu"));
  */
  w.show();

  return app.exec();
}
