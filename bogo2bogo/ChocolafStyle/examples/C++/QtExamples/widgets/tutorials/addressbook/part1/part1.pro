TEMPLATE = app
TARGET = part1
INCLUDEPATH += .

include(../../../../../../../chocolaf/common_files/common.pro)

SOURCES   = addressbook.cpp \
            main.cpp
HEADERS   = addressbook.h

QMAKE_PROJECT_NAME = ab_part1

# install
target.path = $$[QT_INSTALL_EXAMPLES]/widgets/tutorials/addressbook/part1
INSTALLS += target
