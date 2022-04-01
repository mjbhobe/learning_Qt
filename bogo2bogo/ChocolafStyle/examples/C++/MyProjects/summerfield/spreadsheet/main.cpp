#include <QApplication>

#include "chocolaf.h"
#include "mainwindow.h"

int main(int argc, char *argv[])
{
    Chocolaf::ChocolafApp app(argc, argv);
	app.setStyle("Chocolaf");
	
    MainWindow mainWin;
    mainWin.show();
    
	return app.exec();
}
