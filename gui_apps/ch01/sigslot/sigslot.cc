// sigslot/main.cc
#include <QApplication>
#include <QLabel>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>

int main(int argc, char **argv)
{
  QApplication app(argc, argv);

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
  //l2->setContentsMargins(3,3,3,3);
  l2->addLayout(l1);
  window.setLayout(l2);

  // setup signals & slots
  QObject::connect(btn, SIGNAL(clicked()), qApp, SLOT(quit()));

  window.show();
  return app.exec();
}

