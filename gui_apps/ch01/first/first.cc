// -------------------------------------------------------------------------
// first.cc: Hello World with Qt
// this application creates a small window & displays a welcome message
// to the user along with the version of the Qt Framework in use.
//
// @author: Manish Bhobe
// My experiments with C++ & Qt Framework
// This code is meant for learning & educational purposes only!!
// -------------------------------------------------------------------------
#include <QApplication>
#include <QDesktopWidget>
#include <QLabel>
#include <QString>
#include <QTextStream>
#include <QVBoxLayout>

void showCenteredOnDesktop(QWidget &window)
{
   // center window on desktop
   // @see: http://www.qtcentre.org/threads/43158-How-to-center-main-window-on-screen
   window.show();
   QRect screenSize = QApplication::desktop()->screenGeometry();
   int x = (screenSize.width() - window.width()) / 2;
   int y = (screenSize.height() - window.height()) / 2;
   window.move(x, y);
}

int main(int argc, char **argv)
{
   QApplication app(argc, argv);

   // create & show the GUI
   QWidget window;
   window.setWindowTitle("Hello Qt World!");
   QString ver;
   QTextStream out(&ver);
   // is actually populating the underlying QString
   out << "You are using Qt " << QT_VERSION_STR;
   QLabel *version = new QLabel(ver);
   QVBoxLayout *l = new QVBoxLayout;
   l->addWidget(new QLabel("Hello World! Welcome to the Qt Framework."));
   l->addWidget(version);
   window.setLayout(l);

   // window.show();
   showCenteredOnDesktop(window);

   return app.exec();
}
