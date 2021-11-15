// tempConverter/main.cc

// @see: https://vicrucann.github.io/tutorials/osg-qt-high-dpi/

#include "tempConverterDialog.hxx"
#include <QApplication>
#include <windows.h>
#include <winuser.h>

int main(int argc, char **argv)
{
   // QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#ifdef Q_OS_WIN
   SetProcessDPIAware(); // call before the main event loop
#endif                   // Q_OS_WIN

#if QT_VERSION >= QT_VERSION_CHECK(5, 6, 0)
   // disable High DPI scaling as it does not work as expected!
   QApplication::setAttribute(Qt::AA_DisableHighDpiScaling);
#else
   qputenv("QT_DEVICE_PIXEL_RATIO", QByteArray("1"));
#endif // QT_VERSION

   QApplication app(argc, argv);
   // QFont font("Segoe UI", 12);
   // QApplication::setFont(font);

   // initialize & display dialog
   TempConverterDialog dlg;
   dlg.setAttribute(Qt::WA_QuitOnClose);
   dlg.show();

   return app.exec();
}
