// ---------------------------------------------------------------------------
// ch01/layout/main.cc: illustrated use of layouts
// This application will create 4 QLabels and lay them out on a QGridLayout
// which is itself enclosed in a QVBoxLayout
// ---------------------------------------------------------------------------
#include <QApplication>
#include <QDesktopWidget>
#include <QGridLayout>
#include <QLabel>
#include <QString>
#include <QVBoxLayout>

/**
 * @brief centers a widget on the desktop
 * @param
 * 	window - C++ reference the QWidget to center on desktop
 * @returns
 * 	none
 */
void showCenteredOnDesktop(QWidget &window)
{
   window.show();
   QRect screenSize = QApplication::desktop()->screenGeometry();
   int x = (screenSize.width() - window.width()) / 2;
   int y = (screenSize.height() - window.height()) / 2;
   window.move(x, y);
}

int main(int argc, char **argv)
{
   QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
   QApplication app(argc, argv);
   QFont font("SF UI Text", 10);
   QApplication::setFont(font);

   // create & show the GUI
   QWidget window;
   window.setWindowTitle("Qt Layouts Example");
   QVBoxLayout *layout = new QVBoxLayout;

   QString messages[] = {"Hello", "World", "Welcome", "to the awesome Qt Framework"};
   QGridLayout *glayout = new QGridLayout();
   glayout->setHorizontalSpacing(5);
   glayout->setVerticalSpacing(5);
   // layout the first 3 strings horizontally in the first row
   glayout->addWidget(new QLabel(messages[0]), 0, 0);
   glayout->addWidget(new QLabel(messages[1]), 0, 1);
   glayout->addWidget(new QLabel(messages[2]), 0, 2);
   // the 4th string is layed out in the second row, spanning all three cols
   QLabel *lbl = new QLabel(messages[3]);
   lbl->setAlignment(Qt::AlignCenter);
   glayout->addWidget(lbl, 1, 0, 1, 3);
   layout->addLayout(glayout);
   window.setLayout(layout);
   showCenteredOnDesktop(window);

   return app.exec();
}
