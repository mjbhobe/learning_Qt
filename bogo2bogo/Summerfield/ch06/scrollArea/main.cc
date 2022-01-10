#include <QtCore>
#include <QtGui>
#include <QtWidgets>
#include "common_funcs.h"

int main(int argc, char **argv)
{
  QApplication app(argc, argv);

  if (argc != 2) {
    QMessageBox::critical(nullptr, "ERROR-missing parameter",
        QString("Expecting image file name to view in the viewer\r\n"));
    return -1;
  }
  
  if (!QFile::exists(argv[1])) {
    QMessageBox::critical(nullptr, "ERROR-missing parameter",
        QString("Unable to open file - path %1 does not exist!").arg(argv[1]));
    return -1;
  }

  app.setStyle("Fusion");
  app.setFont(QApplication::font("QMenu"));

  QMainWindow window;
  ThemeSwitcher::setDarkTheme(&window);

  QLabel *label = new QLabel; // new QLabel(QString("Hello World! Will display image %1").arg(argv[1]));
  QImage image;
  image.load(argv[1]);
  label->setPixmap(QPixmap::fromImage(image));
  // QScrollArea here..
  QScrollArea *scrollArea = new QScrollArea();
  scrollArea->setWidget(label);
  scrollArea->viewport()->setBackgroundRole(QPalette::Dark);
  scrollArea->viewport()->setAutoFillBackground(true);

  window.setCentralWidget(scrollArea);
  window.setWindowTitle(QString("QScrollArea Demo: %1").arg(argv[1]));
  window.resize(640, 480);
  window.show();

  return app.exec();
}
