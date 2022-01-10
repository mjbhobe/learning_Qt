CONFIG      += plugin debug_and_release
TARGET      = $$qtLibraryTarget(mywidgetcollectionplugin)
TEMPLATE    = lib

HEADERS     = MyLabelPlugin.h MyFramePlugin.h MyWidgetCollection.h
SOURCES     = MyLabelPlugin.cpp MyFramePlugin.cpp MyWidgetCollection.cpp
RESOURCES   = icons.qrc
LIBS        += -L. 

greaterThan(QT_MAJOR_VERSION, 4) {
    QT += designer
} else {
    CONFIG += designer
}

target.path = $$[QT_INSTALL_PLUGINS]/designer
INSTALLS    += target

include(myframe.pri)
include(mylabel.pri)
