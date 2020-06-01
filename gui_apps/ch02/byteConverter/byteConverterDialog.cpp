// byteConverter/byteConverterDialog.cxx
#include "byteConverterDialog.hxx"
#include <QApplication>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QIntValidator>
#include <QLabel>
#include <QLineEdit>
#include <QPalette>
#include <QPushButton>
#include <QRegExpValidator>
#include <QToolTip>
#include <QVBoxLayout>

// helper function
void setReadOnly(QLineEdit &lineEdit, bool readOnly = true)
{
   QPalette palette = lineEdit.palette();
   QPalette::ColorGroup colorGroup = readOnly ? QPalette::Disabled : QPalette::Active;
   QColor textColor = palette.color(colorGroup, QPalette::WindowText);
   QColor backColor = palette.color(colorGroup, QPalette::Base);
   palette.setColor(QPalette::Base, backColor);
   palette.setColor(QPalette::WindowText, textColor);
   lineEdit.setReadOnly(readOnly);
   lineEdit.setPalette(palette);
}

ByteConverterDialog::ByteConverterDialog()
{
   // set title of dialog
   setWindowTitle(tr("Qt: Byte Converter"));

   // define the labels & edit controls
   QString strPrompt("Type in a decimal number (8 digits max) into\n"
                     "the decimal field to see hex & binary values");
   QLabel *prompt = new QLabel(strPrompt);
   QLabel *decLabel = new QLabel(tr("Decimal:"));
   QLabel *hexLabel = new QLabel(tr("Hex:"));
   QLabel *binLabel = new QLabel(tr("Binary:"));
   decEdit = new QLineEdit;
   hexEdit = new QLineEdit;
   binEdit = new QLineEdit;
   // set their validators
   // QIntValidator *intValidator = new QIntValidator(0, 255, decEdit);
   QRegExp dx("[0-9]{0,8}"); // upto 8 decimal digits 0-9
   QRegExpValidator *intValidator = new QRegExpValidator(dx, decEdit);
   decEdit->setValidator(intValidator);
   QRegExp hx("[0-9A-Fa-f]{1,2}"); // allowe 2 hex chars
   QRegExpValidator *hexValidator = new QRegExpValidator(hx, hexEdit);
   hexEdit->setValidator(hexValidator);
   QRegExp bx("[0-1]{1,8}"); // allow 8 binary chars
   QRegExpValidator *binValidator = new QRegExpValidator(bx, binEdit);
   binEdit->setValidator(binValidator);
   QPushButton *quitBtn = new QPushButton(tr("Quit"));
   quitBtn->setDefault(true);
   quitBtn->setToolTip("Click to Exit");

   // set the hex & bin edits as readOnly
   setReadOnly(*hexEdit);
   setReadOnly(*binEdit);

   // set layout
   // top row - prompt
   QHBoxLayout *promptLayout = new QHBoxLayout();
   promptLayout->addWidget(prompt);
   // middle section: labels + edits in grid layout
   QGridLayout *editLayout = new QGridLayout();
   editLayout->addWidget(decLabel, 0, 0);
   editLayout->addWidget(decEdit, 0, 1);
   editLayout->addWidget(hexLabel, 1, 0);
   editLayout->addWidget(hexEdit, 1, 1);
   editLayout->addWidget(binLabel, 2, 0);
   editLayout->addWidget(binEdit, 2, 1);
   // bottom row - spacer + quitButton
   QHBoxLayout *buttonLayout = new QHBoxLayout();
   buttonLayout->addStretch();
   buttonLayout->addWidget(quitBtn);

   // layout the dialog, with edit grids at the top
   QVBoxLayout *mainLayout = new QVBoxLayout();
   mainLayout->addLayout(promptLayout);
   mainLayout->addLayout(editLayout);
   // mainLayout->addStretch();
   mainLayout->addLayout(buttonLayout);
   setLayout(mainLayout);

   // signals & slots for edits...
   QObject::connect(decEdit, SIGNAL(textChanged(const QString &)), this, SLOT(decChanged(const QString &)));
   // QObject::connect(hexEdit, SIGNAL(textChanged(const QString &)), this, SLOT(hexChanged(const QString&)));
   // QObject::connect(binEdit, SIGNAL(textChanged(const QString &)), this, SLOT(binChanged(const QString&)));

   // clicking quitBtn closes the dialog
   QObject::connect(quitBtn, SIGNAL(clicked()), this, SLOT(accept()));
   // kick off signals & slots
   decEdit->setText("75");
}

void ByteConverterDialog::decChanged(const QString &newValue)
{
   // fires when user enters text in the Decimal edit
   // convert value entered in this text box & update the hex & bin edits
   bool ok;
   int num = newValue.toInt(&ok);

   if (ok) {
      hexEdit->setText("0x" + QString::number(num, 16));
      binEdit->setText("0b" + QString::number(num, 2));
   } else {
      hexEdit->setText("");
      binEdit->setText("");
   }
}

void ByteConverterDialog::hexChanged(const QString &newValue)
{
   bool ok;
   int num = newValue.toInt(&ok, 16);

   if (ok) {
      decEdit->setText(QString::number(num));
      binEdit->setText(QString::number(num, 2));
   } else {
      decEdit->setText("");
      binEdit->setText("");
   }
}

void ByteConverterDialog::binChanged(const QString &newValue)
{
   bool ok;
   int num = newValue.toInt(&ok, 2);

   if (ok) {
      hexEdit->setText(QString::number(num, 16));
      decEdit->setText(QString::number(num));
   } else {
      hexEdit->setText("");
      decEdit->setText("");
   }
}
