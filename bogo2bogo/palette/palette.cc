// palette.cc - dump Windows default palette colors
#include <QtCore>
#include <QtGui>
#include <QtWidgets>
#include "common_funcs.h"

int main(int argc, char **argv)
{
  QApplication app(argc, argv);
  app.setFont(QApplication::font("QMenu"));
  app.setStyle("Fusion");

  // setWinDarkPalette(&app);

  // dump palette here
  qDebug() << "QPalette::Window -> " << getPaletteColor(QPalette::Window).name() << "|"  
    << QColor(53,53,53).name(); // and corresponding dark palette setting's color 
  qDebug() << "QPalette::WindowText -> " << getPaletteColor(QPalette::WindowText).name() << "|"
    << (QColor(Qt::white)).name();
  qDebug() << "QPalette::WindowText (Disabled) -> " << getPaletteColor(QPalette::Window, QPalette::Disabled).name() << "|"
    << QColor(127,127,127).name();
  qDebug() << "QPalette::Base -> " << getPaletteColor(QPalette::Base).name() << "|"
    << QColor(42,42,42).name();
  qDebug() << "QPalette::AlternateBase -> " << getPaletteColor(QPalette::AlternateBase).name() << "|"
    << QColor(66,66,66).name();
  qDebug() << "QPalette::ToolTipBase -> " << getPaletteColor(QPalette::ToolTipBase).name() << "|"
    << QColor(Qt::white).name();
  qDebug() << "QPalette::ToolTipText -> " << getPaletteColor(QPalette::ToolTipText).name() << "|"
    << QColor(53,53,53).name();
  qDebug() << "QPalette::Text -> " << getPaletteColor(QPalette::Text).name() << "|"
    << QColor(Qt::white).name();
  qDebug() << "QPalette::Text (Disabled) -> " << getPaletteColor(QPalette::Text, QPalette::Disabled).name() << "|"
    << QColor(127, 127, 127).name();
  qDebug() << "QPalette::Dark -> " << getPaletteColor(QPalette::Dark).name() << "|"
    << QColor(127, 127, 127).name();
  qDebug() << "QPalette::Shadow -> " << getPaletteColor(QPalette::Shadow).name() << "|"
    << QColor(20, 20, 20).name();
  qDebug() << "QPalette::Button -> " << getPaletteColor(QPalette::Button).name() << "|"
    << QColor(53, 53, 53).name();
  qDebug() << "QPalette::ButtonText -> " << getPaletteColor(QPalette::ButtonText).name() << "|"
    << QColor(Qt::white).name();
  qDebug() << "QPalette::ButtonText (Disabled) -> " << getPaletteColor(QPalette::ButtonText, QPalette::Disabled).name() << "|"
    << QColor(127, 127, 127).name();
  qDebug() << "QPalette::BrightText -> " << getPaletteColor(QPalette::BrightText).name() << "|"
    << QColor(Qt::red).name();
  qDebug() << "QPalette::Link -> " << getPaletteColor(QPalette::Link).name() << "|"
    << QColor(42, 130, 218).name();
  qDebug() << "QPalette::Highlight -> " << getPaletteColor(QPalette::Highlight).name() << "|"
    << QColor(42, 130, 218).name();
  qDebug() << "QPalette::Disabled (Highlight) -> " << getPaletteColor(QPalette::Highlight, QPalette::Disabled).name() << "|"
    << QColor(80, 80, 80).name();
  qDebug() << "QPalette::HighlightedText -> " << getPaletteColor(QPalette::HighlightedText).name() << "|"
    << QColor(Qt::white).name();
  qDebug() << "QPalette::HighlightedText (Disabled) -> " << getPaletteColor(QPalette::HighlightedText, QPalette::Disabled).name() << "|"
    << QColor(127, 127, 127).name();
  
  QWidget win;
  win.setWindowTitle("Default Palette");
  QLabel *label = new QLabel("Check the debug dump for default palette colors");
  QVBoxLayout *layout = new QVBoxLayout();
  layout->addWidget(label);
  win.setLayout(layout);
  win.show();

  return app.exec();
}

