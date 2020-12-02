// ch01/sigslot2/sigslot2.cc: illustrates a more realistic signal/slot example
#include <QApplication>
#include <QDesktopWidget>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QSlider>
#include <QSpinBox>
#include <QVBoxLayout>

void centerWidgetOnDesktop(QWidget &window)
{
   window.show();
   QRect screenSize = QApplication::desktop()->screenGeometry();
   int x = (screenSize.width() - window.width()) / 2;
   int y = (screenSize.height() - window.height()) / 2;
   window.move(x, y);
}

int main(int argc, char **argv)
{
   // @see: https://doc.qt.io/archives/qt-5.6/qtlabscontrols-highdpi.html
   QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
   QApplication app(argc, argv);
   QFont font("Segoe UI", 12);
   QApplication::setFont(font);

   // build your GUI here....
   QWidget window;
   window.setWindowTitle("Qt Signal Slot Example");
   // window.setGeometry(QRect(QPoint(0, 0), QSize(450, 80)));

   // setup UI elements
   // top-row: label prompt
   QLabel *prompt = new QLabel("Spin the spinbox below & see the "
                               "slider and label getting updated.");
   // middle row: spinner - slider - label
   QSpinBox *spinBox = new QSpinBox();
   spinBox->setRange(-50, 50);
   QSlider *slider = new QSlider(Qt::Horizontal);
   slider->setRange(-50, 50);
   QLabel *label = new QLabel("0");
   // bottom row: stretch + pushbutton
   QPushButton *btnQuit = new QPushButton("Quit");

   // middle row
   QHBoxLayout *hl = new QHBoxLayout();
   hl->addWidget(spinBox);
   hl->addWidget(slider);
   hl->addWidget(label);
   // bottom row
   QHBoxLayout *h2 = new QHBoxLayout();
   h2->addStretch();
   h2->addWidget(btnQuit);
   // main layout
   QVBoxLayout *layout = new QVBoxLayout();
   layout->addWidget(prompt);
   layout->addLayout(hl);
   layout->addLayout(h2);
   window.setLayout(layout);

   // setup signals & slots
   QObject::connect(spinBox, SIGNAL(valueChanged(int)), label, SLOT(setNum(int)));
   QObject::connect(spinBox, SIGNAL(valueChanged(int)), slider, SLOT(setValue(int)));
   QObject::connect(slider, SIGNAL(valueChanged(int)), label, SLOT(setNum(int)));
   QObject::connect(slider, SIGNAL(valueChanged(int)), spinBox, SLOT(setValue(int)));
   QObject::connect(btnQuit, SIGNAL(clicked()), qApp, SLOT(quit()));

   // this will kick off the signals
   spinBox->setValue(0);
   centerWidgetOnDesktop(window);

   return app.exec();
}
