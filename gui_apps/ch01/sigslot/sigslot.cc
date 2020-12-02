// sigslot/main.cc
#include <QApplication>
#include <QDebug>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QVBoxLayout>
#include <QtGlobal>

#ifdef Q_OS_WIN

#include <windows.h>

const float DEFAULT_DPI = 96.0;

float windowsDpiScale()
{
   HDC screen = GetDC(0);
   FLOAT dpiX = static_cast<FLOAT>(GetDeviceCaps(screen, LOGPIXELSX));
   ReleaseDC(0, screen);
   return dpiX / DEFAULT_DPI;
}

auto DPI_SCALE_FACTOR = windowsDpiScale();

#else

// don't use DPI scaling
auto DPI_SCALE_FACTOR = 1.0;

#endif // Q_OS_WIN

class QMyGuiApplication : public QGuiApplication
{
 public:
   QMyGuiApplication(int &argc, char **argv, QString defaultFontName = "SF UI Text") : QGuiApplication(argc, argv)
   {
      // setAttribute(Qt::AA_EnableHighDpiScaling);
      QFont font(defaultFontName);
      QApplication::setFont(font);
   }
};

int main(int argc, char **argv)
{
   // @see: https://www.qt.io/blog/2016/01/26/high-dpi-support-in-qt-5-6
   // and https://stackoverflow.com/questions/45348571/set-system-environment-variable-before-qt-application-start
   // qputenv("QT_SCALE_FACTOR", "1.2");
   QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
   QApplication app(argc, argv);
   QFont font("Segoe UI", 12);
   QApplication::setFont(font);

#if defined WIN32 || defined WIN64
   qDebug() << "You have a Windows build!" << Qt::endl;
#endif

   QWidget window;
   window.setWindowTitle("Qt: Signals & Slots");
   QLabel *label = new QLabel("Click the button to quit application!");
   QPushButton *btn = new QPushButton("Quit!");
   btn->setDefault(true);
   QHBoxLayout *l1 = new QHBoxLayout;
   l1->addWidget(label);
   l1->addWidget(btn);
   QVBoxLayout *l2 = new QVBoxLayout;
   // set a margin of 3 px all around (instead of default)
   // l2->setContentsMargins(3,3,3,3);
   l2->addLayout(l1);
   window.setLayout(l2);

   // setup signals & slots
   QObject::connect(btn, SIGNAL(clicked()), qApp, SLOT(quit()));

   window.show();
   return app.exec();
}
