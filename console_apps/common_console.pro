######################################################################
# Automatically generated by qmake (2.01a) Fri Sep 25 00:57:07 2015
######################################################################

# DEPENDPATH += .
INCLUDEPATH += .

# The following define makes your compiler warn you if you use any
# feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS
win32 {
    COMMON_FILES_HOME = c:/Dev/Code/git-projects/learning_Qt/bogo2bogo/ChocolafStyle/chocolaf
    LIBS += -lUser32 -lGdi32 -lKernel32 -lDwmapi
}
unix {
    COMMON_FILES_HOME = /home/mjbhobe/code/git-projects/learning_Qt/bogo2bogo/ChocolafStyle/chocolaf
}
INCLUDEPATH += $${COMMON_FILES_HOME}/common_files

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++20 console
QT += core xml sql network
QT -= gui
greaterThan(QT_MAJOR_VERSION, 4): QT -= widgets

win32 {
    CONFIG(msys2) {
       message("Using MSYS2 configuration...")
       INCLUDEPATH += C:/Dev/msys64/mingw64/include
       INCLUDEPATH += C:/Dev/msys64/mingw64/include/opencv4
       QMAKE_LIB_DIRS = -LC:/Dev/msys64/mingw64/lib
       OPENCV_LIBS = -lopencv_core -lopencv_imgproc -lopencv_highgui -lopencv_ml -lopencv_video \
         -lopencv_features2d -lopencv_calib3d -lopencv_objdetect -lopencv_videoio -lopencv_imgcodecs -lopencv_flann
    } else {
       message("**NOT** using MSYS2 configuration...")
       INCLUDEPATH += C:/Dev/GNULibs/gmp-6.2.1/bin/include
       INCLUDEPATH += C:/Dev/OpenCV/build/x86/mingw/install/include
       QMAKE_LIB_DIRS = -LC:/Dev/GNULibs/gmp-6.2.1/bin/lib -LC:/Dev/OpenCV/build/x86/mingw/install/x64/mingw/lib
       OPENCV_LIBS = -lopencv_core451 -lopencv_imgproc451 -lopencv_highgui451 -lopencv_ml451 -lopencv_video451 \
         -lopencv_features2d451 -lopencv_calib3d451 -lopencv_objdetect451 -lopencv_videoio451 -lopencv_imgcodecs451 -lopencv_flann451
    }
}
unix {
    message("Settings for Linux build")
# include for gmp.h & gmpxx.h
    INCLUDEPATH += /usr/local/include
# for opencv includes
    INCLUDEPATH += /usr/include/opencv4
    OPENCV_LIBS = -lopencv_core -lopencv_imgproc -lopencv_highgui -lopencv_ml -lopencv_video \
         -lopencv_features2d -lopencv_calib3d -lopencv_objdetect -lopencv_videoio -lopencv_imgcodecs -lopencv_flann
}

STD_LIBS = -lm -lstdc++
GMP_LIBS = -lgmp -lgmpxx

QMAKE_CXXFLAGS += -pedantic -Wall
QMAKE_LIBS += $${QMAKE_LIB_DIRS} $${STD_LIBS} $${GMP_LIBS} $${OPENCV_LIBS}

# disable qDebug() output in release builds
CONFIG(release, debug|release): DEFINES += QT_NO_DEBUG_OUTPUT

SOURCES += $${COMMON_FILES_HOME}/common_files/common_funcs.cpp
HEADERS += $${COMMON_FILES_HOME}/common_files/common_funcs.h $${COMMON_FILES_HOME}/common_files/common_funcs.argparse/argparse.hpp
