// tempConverter/main.cc
#include "tempConverterDialog.hxx"
#include <QApplication>

int main(int argc, char **argv)
{
   QApplication app(argc, argv);

   // initialize & display dialog
   TempConverterDialog dlg;
   dlg.setAttribute(Qt::WA_QuitOnClose);
   dlg.show();

   return app.exec();
}
