// MainWidget.cc
#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QSpinBox>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include "MainWidget.h"

MainWidget::MainWidget(QWidget *parent /*=nullptr*/)
  : QWidget(parent)
{
  setupUi();
}

void MainWidget::setupUi()
{
  label1 = new QLabel("Celcius Temp:");
  spinBox = new QSpinBox();
  spinBox->setRange(-100,100);
  faren = new QLabel("<html>&deg;F</html>");
  QString ver = QString("Using Qt %1").arg(QT_VERSION_STR);
  version = new QLabel(ver);
  quit = new QPushButton("Quit");
  quit->setToolTip("Quit Application");

  // layout the controls
  auto layout1 = new QHBoxLayout();
  layout1->addWidget(label1);
  layout1->addWidget(spinBox);
  layout1->addWidget(faren);
  auto layout2 = new QHBoxLayout();
  layout2->addWidget(version);
  layout2->addStretch();
  layout2->addWidget(quit);

  auto layout = new QVBoxLayout();
  layout->addLayout(layout1);
  layout->addLayout(layout2);
  setLayout(layout);

  // setup signals & slots
  QObject::connect(quit, &QPushButton::clicked,
    qApp, &QApplication::quit);
  QObject::connect(spinBox,
    static_cast<void(QSpinBox::*)(int)>(&QSpinBox::valueChanged),
    this, &MainWidget::convertTemp);

  this->setFont(QApplication::font("QMenu"));

  // trigger the signals & Slots
  spinBox->setValue(32);
}

void MainWidget::convertTemp()
{
  auto celcius = this->spinBox->value();
  auto farenTemp = static_cast<double>(((9.0/5.0) * celcius) + 32.0f);
  QString s1 = QString("<html><b>%1</b> &deg;F</html>").
    arg(farenTemp, 0, 'f', 2); // *.3f formatter
  faren->setText(s1);
}
