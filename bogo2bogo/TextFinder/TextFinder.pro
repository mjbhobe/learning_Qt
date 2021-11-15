TEMPLATE = app
TARGET = TextFinder

include (../common.pro)

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disabl `es all the APIs deprecated before Qt 6.0.0

SOURCES += \
    main.cpp \
    Textfinder.cpp

HEADERS += \
    Textfinder.h

FORMS += \
  TextFinder.ui

RESOURCES += \
   TextFinder.qrc

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
