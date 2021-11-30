#ifndef CONTROLLERWIDGET_H
#define CONTROLLERWIDGET_H

#include <QWidget>
class QGroupBox;
class QPushButton;
class QRadioButton;
class QCheckBox;
class PreviewWindow;

QT_BEGIN_NAMESPACE
namespace Ui {
class Widget;
}
QT_END_NAMESPACE

class ControllerWidget : public QWidget
{
  Q_OBJECT

public:
  ControllerWidget(QWidget *parent = nullptr);

private slots:
  void updatePreview();

private:
  void createTypeGroupBox();
  void createHintsGroupBox();
  QCheckBox *createCheckBox(const QString &text);
  QRadioButton *createRadioButton(const QString &text);

  PreviewWindow *previewWindow;

  QGroupBox *typeGroupBox;
  QGroupBox *hintsGroupBox;
  QPushButton *quitButton;

  QRadioButton *windowRadioButton;
  QRadioButton *dialogRadioButton;
  QRadioButton *sheetRadioButton;
  QRadioButton *drawerRadioButton;
  QRadioButton *popupRadioButton;
  QRadioButton *toolRadioButton;
  QRadioButton *toolTipRadioButton;
  QRadioButton *splashScreenRadioButton;

  QCheckBox *msWindowsFixedSizeDialogCheckBox;
  QCheckBox *x11BypassWindowManagerCheckBox;
  QCheckBox *framelessWindowCheckBox;
  QCheckBox *windowNoShadowCheckBox;
  QCheckBox *windowTitleCheckBox;
  QCheckBox *windowSystemMenuCheckBox;
  QCheckBox *windowMinimizeButtonCheckBox;
  QCheckBox *windowMaximizeButtonCheckBox;
  QCheckBox *windowCloseButtonCheckBox;
  QCheckBox *windowContextHelpButtonCheckBox;
  QCheckBox *windowShadeButtonCheckBox;
  QCheckBox *windowStaysOnTopCheckBox;
  QCheckBox *windowStaysOnBottomCheckBox;
  QCheckBox *customizeWindowHintCheckBox;
};
#endif // CONTROLLERWIDGET_H
