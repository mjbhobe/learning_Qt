TARGET = mv_tree
TEMPLATE = app
QT += widgets
requires(qtConfig(treeview))
SOURCES += main.cpp \
    mainwindow.cpp
HEADERS += mainwindow.h

# install
target.path = $$[QT_INSTALL_EXAMPLES]/widgets/tutorials/modelview/6_treeview
INSTALLS += target
