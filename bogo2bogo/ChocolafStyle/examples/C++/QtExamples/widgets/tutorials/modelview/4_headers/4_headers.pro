TARGET = mv_headers
TEMPLATE = app
INCLUDEPATH += .
include(../../../../../../../chocolaf/common_files/common.pro)

# requires(qtConfig(tableview))

SOURCES += main.cpp  \
           mymodel.cpp

HEADERS += mymodel.h

# install
target.path = $$[QT_INSTALL_EXAMPLES]/widgets/tutorials/modelview/4_headers
INSTALLS += target
