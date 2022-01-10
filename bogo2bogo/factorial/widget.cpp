#include "widget.h"
#include <cassert>
#include <climits>
#include <gmpxx.h>
#include <QApplication>
#include <QByteArray>
#include <QDebug>
#include <QFont>
#include <QHBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
#include <QRegExp>
#include <QRegExpValidator>
#else
#include <QRegularExpression>
#include <QRegularExpressionValidator>
#endif
#include <QString>
#include <QTextEdit>
#include <QTextStream>
#include <QVBoxLayout>

Widget::Widget(QWidget *parent) : QWidget(parent)
{
   label = new QLabel("Number:");
   number = new QLineEdit();
   calculate = new QPushButton("Calculate");
   quit = new QPushButton("Quit!");
   factorial = new QTextEdit("");
   setupUi();
   resize(640, 480);
}

void Widget::setupUi()
{
   this->setWindowTitle("Qt Factorial");

   QHBoxLayout *layout1 = new QHBoxLayout();
   layout1->addWidget(label);
   layout1->addWidget(number);
   layout1->addWidget(calculate);
   layout1->addWidget(quit);

   QVBoxLayout *main = new QVBoxLayout();
   main->addLayout(layout1);
   main->addWidget(factorial);
   this->setLayout(main);

   calculate->setToolTip("Calculate factorial");
   calculate->setEnabled(false); // disabled initially
   calculate->setDefault(true);
   quit->setToolTip("Quit application");
   factorial->setReadOnly(true);
   factorial->setEnabled(false);

   // QFont font = QFont(QApplication::font("QMenu").family(),
   //                   QApplication::font("QMenu").pointSize() - 1);
#ifdef Q_OS_WINDOWS
   QFont font = QFont("Consolas");
   font.setPixelSize(12);
#else
   QFont mono = QFont("Monospace");
   QFont font = QFont(mono.family(), mono.pointSize() - 2);
#endif
   factorial->setFont(font);

   QString str, str2;
   QTextStream ostr(&str);
   ostr << ULONG_MAX;
   // max number of digits in ULLONG_MAX
   auto max_len = str.length();
   QTextStream ostr2(&str2);
   ostr2 << "[1-9][0-9]{0," << max_len - 1 << "}";
   qDebug() << "ULONG_MAX length " << max_len << " QRegExp: " << str2;
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
   // for Qt6-
   QRegExp regExp(str2);
   number->setValidator(new QRegExpValidator(regExp, this));
#else
   // for Qt6+
   QRegularExpression regExp(str2);
   number->setValidator(new QRegularExpressionValidator(regExp, this));
#endif

   // setup signals & slots - we'll use lamda functions here
   connect(number, &QLineEdit::textChanged,
           [=](const QString &text) { calculate->setEnabled(!text.isEmpty()); });
   connect(quit, &QPushButton::clicked, qApp, &QApplication::quit);
   connect(calculate, &QPushButton::clicked, this, &Widget::calculateFactorial);
}

Widget::~Widget() {}

void Widget::calculateFactorial()
{
   // clear any existing factorial value displayed
   factorial->clear();

   QApplication::setOverrideCursor(Qt::WaitCursor);
   bool ok;
   unsigned long num = number->text().toULong(&ok, 10);

   if (ok) {
      mpz_class fact = mpz_class::factorial(num);
      QString strFactorial = QString(fact.get_str().c_str());
      factorial->setText(strFactorial);
   }
   else {
      factorial->setText("Can't convert input");
   }
   QApplication::restoreOverrideCursor();
}
