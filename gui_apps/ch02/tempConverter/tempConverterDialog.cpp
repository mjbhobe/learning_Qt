// tempConverterDialog.cpp - implementation file
#include "tempConverterDialog.hxx"
#include "tempConverter.hxx"
#include <QDialog>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QSlider>
#include <QSpinBox>
#include <QVBoxLayout>

TempConverterDialog::TempConverterDialog(QWidget *parent)
   : QDialog(parent)
{
   QLabel *l1 = new QLabel("<html>Spin/Enter Temperature &deg;C:</html>");
   _spinner = new QSpinBox(this);
   QLabel *l2 = new QLabel("<html>&deg;F:</html>");
   _slider = new QSlider(Qt::Horizontal, this);
   _temp = new QLabel("temp", this);
   QPushButton *quitBtn = new QPushButton("Quit", this);
   _tempConverter = new TempConverter(this);

   // top layout, with spinner, slider & label
   QHBoxLayout *top = new QHBoxLayout();
   top->addWidget(l1);
   top->addStretch();
   top->addWidget(_spinner);

   // middle layout with Faren converters
   QHBoxLayout *middle = new QHBoxLayout();
   middle->addWidget(l2);
   middle->addWidget(_slider);
   middle->addWidget(_temp);

   // bottom Hbox with pushbutton to right
   QHBoxLayout *bot = new QHBoxLayout;
   bot->addStretch();
   bot->addWidget(quitBtn);

   // main layout
   QVBoxLayout *main = new QVBoxLayout;
   main->addLayout(top);
   main->addLayout(middle);
   main->addLayout(bot);
   setLayout(main);
   setWindowTitle("Temperature Converter");

   // connect signals & slots
   QObject::connect(_spinner,
      SIGNAL(valueChanged(const QString &)),
      _tempConverter,
      SLOT(setTemp(const QString &)));
   QObject::connect(_tempConverter, SIGNAL(tempChanged(int)), _slider, SLOT(setValue(int)));
   QObject::connect(
      _tempConverter, SIGNAL(tempChanged(const QString &)), _temp, SLOT(setText(const QString &)));
   QObject::connect(quitBtn, SIGNAL(clicked()), this, SLOT(accept()));

   _spinner->setRange(-100, 100);
   int minSlider = static_cast<int>(_tempConverter->convert(-100));
   int maxSlider = static_cast<int>(_tempConverter->convert(100));
   _slider->setRange(minSlider, maxSlider);
   _slider->setEnabled(false);
   // start with converting 10C to F
   _spinner->setValue(10);
}
