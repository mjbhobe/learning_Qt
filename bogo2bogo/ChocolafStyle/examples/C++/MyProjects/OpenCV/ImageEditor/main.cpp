#include <QtCore>
#include <QtGui>
#include <QtWidgets>

#include "ImageEditor.h"
#include "common_funcs.h"
#include "chocolaf.h"

int main(int argc, char *argv[])
{
   Chocolaf::ChocolafApp app(argc, argv);
   app.setStyle("Chocolaf");

   ImageEditor w;
   w.show();

   return app.exec();
}
