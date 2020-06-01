// tempConverter.hxx - TempConverter class
#ifndef __TempConverter_hxx__
#define __TempConverter_hxx__

#include <QDebug>
#include <QObject>

#define myqDebug() qDebug() << fixed << qSetRealNumberPrecision(3)

class TempConverter : public QObject
{
   Q_OBJECT
public:
   enum TempConvType { C2F, F2C };

protected:
   TempConvType _convType;

public:
   TempConverter(QObject *parent = nullptr, TempConvType convType = TempConverter::C2F);
   float convert(float temp);
public slots:
   void setTemp(const QString &temp2Conv);
signals:
   void tempChanged(int convTemp);
   void tempChanged(const QString &convTemp);
};

#endif // __TempConverter_hxx__
