// fileFindDlg.cc - find files dialog implementation
//
#include <QtCore>
#include <QtGui>
#include <QtWidgets>

FildFindDialog::FileFindDialog(QWidget *parent/*= nullptr*/)
  : QDialog(parent)
{
  namedLabel = new QLabel("Named:");
  namedLineEdit = new QLineEdit;
  lookInLabel = new QLabel("Look In:");

