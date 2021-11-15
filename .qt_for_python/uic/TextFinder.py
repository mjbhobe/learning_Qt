# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TextFinder.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_TextFinder(object):
    def setupUi(self, TextFinder):
        if not TextFinder.objectName():
            TextFinder.setObjectName(u"TextFinder")
        TextFinder.resize(459, 443)
        self.verticalLayout_2 = QVBoxLayout(TextFinder)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(TextFinder)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.findText = QLineEdit(TextFinder)
        self.findText.setObjectName(u"findText")

        self.horizontalLayout.addWidget(self.findText)

        self.findButton = QPushButton(TextFinder)
        self.findButton.setObjectName(u"findButton")

        self.horizontalLayout.addWidget(self.findButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(TextFinder)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.findText)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.findText, self.findButton)
        QWidget.setTabOrder(self.findButton, self.textEdit)

        self.retranslateUi(TextFinder)

        QMetaObject.connectSlotsByName(TextFinder)
    # setupUi

    def retranslateUi(self, TextFinder):
        TextFinder.setWindowTitle(QCoreApplication.translate("TextFinder", u"Form", None))
        self.label.setText(QCoreApplication.translate("TextFinder", u"&Keyword", None))
        self.findButton.setText(QCoreApplication.translate("TextFinder", u"&Find", None))
    # retranslateUi

