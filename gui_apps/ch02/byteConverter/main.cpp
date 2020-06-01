// byteConverter/main.cc
#include "byteConverterDialog.hxx"
#include <QApplication>

int main(int argc, char **argv)
{
   QApplication app(argc, argv);

   // initialize & display dialog
   ByteConverterDialog dlg;
   dlg.setAttribute(Qt::WA_QuitOnClose);
   dlg.show();

   return app.exec();
}
