// pyqtapp.h - declared helper PyQtApp class
#ifndef __Chocolaf_PyQtApp_h__
#define __Chocolaf_PyQtApp_h__

#include "chocolaf_palettes.h"
#include <QApplication>
#include <QMap>
#include <QPalette>
#include <QString>

class PyQtApp : public QApplication
{
 public:
   PyQtApp(int, char **);
   void setStyle(const QString &styleName);

   QPalette *getPalette(const QString &key = "Chocolaf");
   QPalette *getStylesheet(const QString &key = "Chocolaf");

 protected:
   QMap<QString, QString> _styleSheets;
   QMap<QString, QPalette *> _palettes;
   QString loadStylesheet();
};

#endif // __Chocolaf_PyQtApp_h__
