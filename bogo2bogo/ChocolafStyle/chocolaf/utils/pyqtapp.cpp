// pyqtapp.cpp - PyQtApp class implementation
#include "pyqtapp.h"
#include <QApplication>

PyQtApp::PyQtApp(int argc, char **argv) : QApplication(argc, argv) { this->setFont(QApplication::font("QMenu")); }
