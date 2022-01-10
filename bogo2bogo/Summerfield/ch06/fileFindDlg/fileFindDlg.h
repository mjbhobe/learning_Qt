// fileFindDlg.h - find dialog
#ifndef __Qt_Summerfield_FileFindDialog__
#define __Qt_Summerfield_FileFindDialog__

#include <QDialog>
class QLabel;
class QLineEdit;
class QTableWidget;
class QCheckBox;
class QPushButton;

class FileFindDialog : public QDialog
{
      Q_OBJECT
  private:
      QLabel *namedLabel;
      QLineEdit *namedLineEdit;
      QLabel *lookInLabel;
      QLineEdit *lookInLineEdit;
      QLabel *messageLabel;
      QPushButton *findButton;
      QPushButton *stopButton;
      QPushButton *closeButton;
      QPushButton *helpButton;

      void setupUi();

  public:
      FileFindDialog(QWidget *parent=nullptr);
};


#endif   // __Qt_Summerfield_FileFindDialog__
