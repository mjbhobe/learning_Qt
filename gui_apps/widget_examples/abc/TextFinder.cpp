#include "TextFinder.h"
#include "ui_TextFinder.h"
#include <QApplication>
#include <QFile>
#include <QString>
#include <QTextCursor>
#include <QTextStream>
#include <QWidget>

TextFinder::TextFinder(QWidget *parent)
    : QWidget(parent), ui(new Ui::TextFinder)
{
    ui->setupUi(this);
    loadTextFile();

    // setup signals & slots
    QObject::connect(ui->findButton, SIGNAL(clicked()),
        this, SLOT(onFindButtonClicked()));
}

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
    QString searchString = ui->findText->text();
    ui->textEdit->find(searchString, QTextDocument::FindWholeWords);
}
