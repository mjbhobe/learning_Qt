#include "MainWindow.h"
#include "ui_MainWindow.h"
#include <QDebug>
#include <QMap>

const QMap<QString, QString> quotes
  = {{"Nelson Mandela",
      "The greatest glory in living lies not in never falling, but in rising every time we fall."},
     {"Walt Disney", "The way to get started is to quit talking and begin doing."},
     {"Steve Jobs",
      "Your time is limited, so don\'t waste it living someone else\'s life."
      "Don\'t be trapped by dogma – which is living with the results of other people\'s thinking."},
     {"Eleanor Roosevelt",
      "If life were predictable it would cease to be life, and be without flavor."},
     {"Oprah Winfrey", "If you look at what you have in life, you\'ll always have more. If you "
                       "look at what you don\'t have in life, you\'ll never have enough."},
     {"James Cameron", "If you set your goals ridiculously high and it\'s a failure, you will "
                       "fail above everyone else\'s success."},
     {"John Lennon", "Life is what happens when you\'re busy making other plans."}};

MainWindow::MainWindow(QWidget *parent)
  : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
  ui->setupUi(this);

  auto oses = (QStringList() << "Windows"
                             << "MacOs"
                             << "Linux"
                             << "Ubuntu"
                             << "Kubuntu");
  oses.sort();
  ui->osComboBox->addItems(oses);

  connect(ui->closeButton, &QPushButton::clicked, QApplication::instance(), &QApplication::exit);
  connect(ui->osComboBox, QOverload<int>::of(&QComboBox::currentIndexChanged), [=](int) {
    ui->lineEdit->setText(QString("You love %1").arg(ui->osComboBox->currentText()));
  });
  ui->osComboBox->setCurrentIndex(1); // trigger above lambda

  foreach (auto &key, quotes.keys()) {
    qDebug() << key;
    ui->quotesCombo->addItem(key);
  }
  ui->quotesCombo->model()->sort(0); // sort keys
  connect(ui->quotesCombo, QOverload<int>::of(&QComboBox::currentIndexChanged), [=](int) {
    QString currSel = ui->quotesCombo->currentText();
    ui->quoteEdit->setText(QString("<html>%1 - <i>%2</i></html>").arg(quotes[currSel]).arg(currSel));
  });
  ui->quotesCombo->setCurrentIndex(5); // trigger above lambda

  ui->horizontalSlider->setValue(25);
  ui->verticalSlider->setValue(75);
  ui->closeButton->setToolTip("Close Application");
}

MainWindow::~MainWindow()
{
  delete ui;
}

