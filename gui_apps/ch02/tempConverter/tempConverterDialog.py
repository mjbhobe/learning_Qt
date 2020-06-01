# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tempConverterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TempConverterDialog(object):
    def setupUi(self, TempConverterDialog):
        TempConverterDialog.setObjectName("TempConverterDialog")
        TempConverterDialog.resize(310, 120)
        font = QtGui.QFont()
        font.setPointSize(10)
        TempConverterDialog.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(TempConverterDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 290, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinCelcius = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinCelcius.setMinimum(-100)
        self.spinCelcius.setMaximum(100)
        self.spinCelcius.setProperty("value", 32)
        self.spinCelcius.setObjectName("spinCelcius")
        self.horizontalLayout.addWidget(self.spinCelcius)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.slideFahren = QtWidgets.QSlider(self.layoutWidget)
        self.slideFahren.setEnabled(False)
        self.slideFahren.setMinimum(-148)
        self.slideFahren.setMaximum(212)
        self.slideFahren.setOrientation(QtCore.Qt.Horizontal)
        self.slideFahren.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slideFahren.setObjectName("slideFahren")
        self.horizontalLayout_2.addWidget(self.slideFahren)
        self.lblFahren = QtWidgets.QLabel(self.layoutWidget)
        self.lblFahren.setObjectName("lblFahren")
        self.horizontalLayout_2.addWidget(self.lblFahren)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnQuit = QtWidgets.QPushButton(self.layoutWidget)
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout_3.addWidget(self.btnQuit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(TempConverterDialog)
        QtCore.QMetaObject.connectSlotsByName(TempConverterDialog)

    def retranslateUi(self, TempConverterDialog):
        _translate = QtCore.QCoreApplication.translate
        TempConverterDialog.setWindowTitle(_translate("TempConverterDialog", "Qt: Temperature Conversion"))
        self.label.setText(_translate("TempConverterDialog", "<html>Spin/Enter temperature in &deg;C</html>"))
        self.label_2.setText(_translate("TempConverterDialog", "<html>&deg;F</html>"))
        self.lblFahren.setText(_translate("TempConverterDialog", "9999"))
        self.btnQuit.setToolTip(_translate("TempConverterDialog", "Quit Application"))
        self.btnQuit.setText(_translate("TempConverterDialog", "Quit!"))
