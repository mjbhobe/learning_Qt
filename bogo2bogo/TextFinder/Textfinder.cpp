#include "Textfinder.h"
#include "ui_Textfinder.h"
#include <QFile>
#include <QTextStream>

TextFinder::TextFinder(QWidget *parent) : QWidget(parent), ui(new Ui::TextFinder)
{
   ui->setupUi(this);
   loadTextFile();

   // setup signals & slots
   ui->textEdit->setReadOnly(true);
   ui->textEdit->setEnabled(false);
   QObject::connect(ui->findButton, SIGNAL(clicked()), this, SLOT(onFindButtonClicked()));
}

TextFinder::~TextFinder() { delete ui; }

void TextFinder::loadTextFile()
{
   QFile inputFile(":/input.txt");
   inputFile.open(QIODevice::ReadOnly);

   QTextStream in(&inputFile);
   QString lines = in.readAll();
   inputFile.close();

   ui->textEdit->setPlainText(lines);
   QTextCursor cursor = ui->textEdit->textCursor();
   cursor.movePosition(QTextCursor::Start, QTextCursor::MoveAnchor, 1);
}

void TextFinder::onFindButtonClicked()
{
   // move cursor to start of file
   QTextCursor cursor = ui->textEdit->textCursor();
   cursor.movePosition(QTextCursor::Start, QTextCursor::MoveAnchor, 1);
   QString searchString = ui->findText->text();
   ui->textEdit->find(searchString, QTextDocument::FindWholeWords);
}
