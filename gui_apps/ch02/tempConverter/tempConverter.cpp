// tempConverter.cpp - TempConverter class implementation
// @author: Manish Bhobe
// My experiments with Qt Framework. Use at your own risk!
#include "tempConverter.hxx"
#include <QDebug>
#include <QObject>
#include <QTextStream>

TempConverter::TempConverter(QObject *parent, TempConverter::TempConvType convType)
   : QObject(parent)
{
   this->_convType = convType;
}

float TempConverter::convert(float temp)
{
   if (this->_convType == C2F) {
      // convert Celcius to Farenheit
      // F = (C * (9.0/5.0)) + 32.0
      auto farenheit = (temp * (9.0 / 5.0)) + 32.0;
      /*
       myqDebug() << "TempConverter::convert(" << temp
       << ") -> Celcius to Farenheit: " << farenheit;
       */
      return float(farenheit);
   }
   else {
      // convert Farehieit to Celcius
      // C = (F - 32.0) / (9.0/5.0)
      auto celcius = (temp - 32.0) / (9.0 / 5.0);
      /*
       myqDebug() << "TempConverter::convert(" << temp
       << ") -> Farenheit to Celcius: " << celcius;
       */
      return float(celcius);
   }
}

// slot
void TempConverter::setTemp(const QString &temp2Conv)
{
   bool bOk;
   float temp2ConvNum = temp2Conv.toDouble(&bOk);
   if (bOk) {
      // qDebug() << "Converting " << temp2ConvNum << "...";
      float convTemp = convert(temp2ConvNum);
      QString convTempStr;
      convTempStr.sprintf("%+.2f", convTemp);
      /*
       qDebug() << "Converted: float = " << convTemp << " and string = "
       << convTempStr;
       */
      emit tempChanged(int(convTemp));
      emit tempChanged(convTempStr);
   }
}
