#include "Textfinder.h"
#include "ui_Textfinder.h"
#include <QFile>
#include <QFileDialog>
#include <QMessageBox>
#include <QStandardPaths>
#include <QTextStream>

QFont monoFont = QFont("Consolas", 10);

TextFinder::TextFinder(QWidget *parent) : QWidget(parent), ui(new Ui::TextFinder)
{
   ui->setupUi(this);
   setWindowIcon(QIcon(":/eye.png")); // load an image
   loadTextFile();

   // setup signals & slots
   ui->textEdit->setReadOnly(true);
   ui->textEdit->setEnabled(false);
   ui->textEdit->setFont(monoFont);
   QObject::connect(ui->findButton, SIGNAL(clicked()), this, SLOT(onFindButtonClicked()));
   QObject::connect(ui->openButton, SIGNAL(clicked()), this, SLOT(onOpenButtonClicked()));
}

TextFinder::~TextFinder() { delete ui; }

void TextFinder::loadTextFile(const QString &filePath /*=""*/)
{
   QFile inputFile((filePath == "") ? ":/input.txt" : filePath);
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

void TextFinder::onOpenButtonClicked()
{
   const QStringList docsLocation = QStandardPaths::standardLocations(
      QStandardPaths::DocumentsLocation);
   QString fileName = QFileDialog::getOpenFileName(
      this, tr("Open File"), docsLocation.last(),
      tr("Text Files (*.txt *.c *.cpp *.h *.hxx *.py *.java *.bat *.sh)"));
   if (fileName != "")
      loadTextFile(fileName);
}
