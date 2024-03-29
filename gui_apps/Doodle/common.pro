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

GMP_INC=`pkg-config --cflags gmp`
GMP_LIBS=`pkg-config --libs gmp`

QMAKE_CXXFLAGS += -pedantic -Wall -IC:/Dev/GNULibs/gmp-6.2.1/bin/include
# QMAKE_CXXFLAGS += -pedantic -Wall -IC:/Dev/msys64/mingw64/include
#QMAKE_LFLAGS += -lgmpxx -lgmp -lstdc++ -lm
#INCLUDEPATH += /home/mjbhobe/anaconda3/envs/dlnlp/include
INCLUDEPATH += ../common
# QMAKE_LIBS += -L/c/Dev/msys64/mingw64/lib -lgmpxx -lgmp -lstdc++ -lm
QMAKE_LIBS += -LC:/Dev/GNULibs/gmp-6.2.1/bin/lib -lgmpxx -lgmp -lstdc++ -lm
# LIBS +=  -lstdc++ -lm $(GMP_LIBS)
HEADERS += ../common/common.hxx
SOURCES += ../common/common.cc

# disable qDebug() output in release builds
CONFIG(release, debug|release): DEFINES += QT_NO_DEBUG_OUTPUT

