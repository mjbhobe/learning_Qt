#include <QtWidgets>

int main(int argc, char **argv)
{
  QApplication app(argc, argv);
  app.setFont(QApplication::font("QMenu"));

  // create the GUI
  QWidget window;
  QLineEdit *lineEdit = new QLineEdit();
  QPushButton *button = new QPushButton("Clear");
  QHBoxLayout *layout = new QHBoxLayout();
  layout->addWidget(lineEdit);
  layout->addWidget(button);

  //QObject::connect(button, SIGNAL(clicked), lineEdit, SLOT(clear));
  QObject::connect(button, &QPushButton::clicked, lineEdit, &QLineEdit::clear);

  window.setLayout(layout);
  window.setWindowTitle("Why?? (C++)");
  window.show();

  return app.exec();
}
