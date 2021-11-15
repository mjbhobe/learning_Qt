# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gotocelldialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_GoToCellDialog(object):
    def setupUi(self, GoToCellDialog):
        if not GoToCellDialog.objectName():
            GoToCellDialog.setObjectName(u"GoToCellDialog")
        GoToCellDialog.resize(261, 82)
        font = QFont()
        font.setPointSize(10)
        GoToCellDialog.setFont(font)
        GoToCellDialog.setFocusPolicy(Qt.TabFocus)
        self.layoutWidget = QWidget(GoToCellDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 241, 28))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(self.layoutWidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.layoutWidget1 = QWidget(GoToCellDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 241, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(GoToCellDialog)

        self.okButton.setDefault(True)


        QMetaObject.connectSlotsByName(GoToCellDialog)
    # setupUi

    def retranslateUi(self, GoToCellDialog):
        GoToCellDialog.setWindowTitle(QCoreApplication.translate("GoToCellDialog", u"Find", None))
        self.okButton.setText(QCoreApplication.translate("GoToCellDialog", u"Ok", None))
        self.cancelButton.setText(QCoreApplication.translate("GoToCellDialog", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("GoToCellDialog", u"&Cell Location:", None))
    # retranslateUi

