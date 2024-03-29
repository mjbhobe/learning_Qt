// ch02/findDialog/findDialog.h: creating dialogs by hand
#ifndef __FindDialog_h__
#define __FindDialog_h__

#include <QDialog>

class QCheckBox;
class QLabel;
class QLineEdit;
class QPushButton;

class FindDialog : public QDialog
{
    Q_OBJECT
  public:
    FindDialog(QWidget *parent = nullptr);

  signals:
    void findNext(const QString& str, Qt::CaseSensitivity cs);
    void findPrevious(const QString& str, Qt::CaseSensitivity cs);

  private slots:
    void findClicked();
    void enableFindButton(const QString& text);

  private:
    QLabel *label;
    QLineEdit *lineEdit;
    QCheckBox *caseCheckBox;
    QCheckBox *backwardCheckBox;
    QPushButton *findButton;
    QPushButton *closeButton;
};

#endif // __FindDialog_h__
