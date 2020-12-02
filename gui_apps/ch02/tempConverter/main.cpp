// tempConverter/main.cc
#include "tempConverterDialog.hxx"
#include <QApplication>

int main(int argc, char **argv)
{
   QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
   QApplication app(argc, argv);
   QFont font("SF UI Text", 10);
   QApplication::setFont(font);

   // initialize & display dialog
   TempConverterDialog dlg;
   dlg.setAttribute(Qt::WA_QuitOnClose);
   dlg.show();

   return app.exec();
}
