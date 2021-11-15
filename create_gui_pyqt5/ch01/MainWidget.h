// MainWidget.h: main widget of Application
#ifndef __MainWidget_h__
#define __MainWidget_h__

#include <QWidget>

class QLabel;
class QSpinBox;
class QPushButton;

class MainWidget : public QWidget {
    Q_OBJECT
  private:
    // members
    QLabel *label1, *version, *faren;
    QSpinBox *spinBox;
    QPushButton *quit;

  protected:
    // functions
    void setupUi();
    void convertTemp();
  public:
    MainWidget(QWidget *parent=nullptr);
};


#endif  // __MainWidget_h__
