// tempConverterDialog.hxx - TempConverter class
#ifndef __TempConverterDialog_hxx__
#define __TempConverterDialog_hxx__

#include <QDialog>
class QSpinBox;
class QSlider;
class QLabel;
class TempConverter;

class TempConverterDialog : public QDialog
{
   Q_OBJECT
protected:
   QSpinBox *_spinner;
   QSlider *_slider;
   QLabel *_temp;
   TempConverter *_tempConverter;

public:
   TempConverterDialog(QWidget *parent = nullptr);
};

#endif // __TempConverter_hxx__
