######################################################################
# Automatically generated by qmake (2.01a) Fri Sep 25 00:57:07 2015
######################################################################

TEMPLATE = app
DEPENDPATH += .
INCLUDEPATH += .

win32 {
  CONFIG += console
}
CONFIG += c++20

QT += core gui xml sql
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

QMAKE_CXXFLAGS += -pedantic -Wall
#QMAKE_LFLAGS += -lgmpxx -lgmp -lstdc++ -lm
#INCLUDEPATH += /home/mjbhobe/anaconda3/envs/dlnlp/include
INCLUDEPATH += ../common
LIBS +=  -lstdc++ -lm #-lgmpxx -lgmp

HEADERS += ../common/common.hxx
SOURCES += ../common/common.cc

# disable qDebug() output in release builds
# CONFIG(release, debug|release): DEFINES += QT_NO_DEBUG_OUTPUT

