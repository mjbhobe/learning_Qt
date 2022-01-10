TEMPLATE = app
TARGET = helloQt6
QT -= gui

CONFIG += c++20 console
CONFIG -= app_bundle

COMMON_FILES_HOME = c:/Dev/Code/git-projects/learning_Qt/bogo2bogo/common_files

INCLUDEPATH += C:/Dev/GNULibs/gmp-6.2.1/bin/include
INCLUDEPATH += $${COMMON_FILES_HOME}
# INCLUDEPATH += C:/Dev/msys64/mingw64/include
INCLUDEPATH += C:/Dev/GNULibs/gmp-6.2.1/bin/include
# QMAKE_LIBS += -LC:/Dev/msys64/mingw64/lib -lstdc++ -lm
QMAKE_LIBS += -LC:/Dev/GNULibs/gmp-6.2.1/bin/lib -lgmp -lgmpxx -lstdc++ -lm

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
        main.cpp

# SOURCES += $${COMMON_FILES_HOME}/common_funcs.cpp
# HEADERS += $${COMMON_FILES_HOME}/common_funcs.h

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
