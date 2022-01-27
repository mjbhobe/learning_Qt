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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_TextFinder(object):
    def setupUi(self, TextFinder):
        if not TextFinder.objectName():
            TextFinder.setObjectName(u"TextFinder")
        TextFinder.resize(781, 585)
        self.verticalLayout = QVBoxLayout(TextFinder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(TextFinder)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.findText = QLineEdit(TextFinder)
        self.findText.setObjectName(u"findText")

        self.horizontalLayout.addWidget(self.findText)

        self.wholeWordsCheck = QCheckBox(TextFinder)
        self.wholeWordsCheck.setObjectName(u"wholeWordsCheck")

        self.horizontalLayout.addWidget(self.wholeWordsCheck)

        self.caseSensitiveCheck = QCheckBox(TextFinder)
        self.caseSensitiveCheck.setObjectName(u"caseSensitiveCheck")

        self.horizontalLayout.addWidget(self.caseSensitiveCheck)

        self.findButton = QPushButton(TextFinder)
        self.findButton.setObjectName(u"findButton")
        self.findButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.findButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(TextFinder)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFocusPolicy(Qt.NoFocus)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.openButton = QPushButton(TextFinder)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout_2.addWidget(self.openButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.findText)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.findText, self.wholeWordsCheck)
        QWidget.setTabOrder(self.wholeWordsCheck, self.caseSensitiveCheck)
        QWidget.setTabOrder(self.caseSensitiveCheck, self.findButton)
        QWidget.setTabOrder(self.findButton, self.openButton)
        QWidget.setTabOrder(self.openButton, self.textEdit)

        self.retranslateUi(TextFinder)

        self.findButton.setDefault(True)


        QMetaObject.connectSlotsByName(TextFinder)
    # setupUi

    def retranslateUi(self, TextFinder):
        TextFinder.setWindowTitle(QCoreApplication.translate("TextFinder", u"Form", None))
        self.label.setText(QCoreApplication.translate("TextFinder", u"&Search", None))
#if QT_CONFIG(tooltip)
        self.wholeWordsCheck.setToolTip(QCoreApplication.translate("TextFinder", u"Search for whole words only", None))
#endif // QT_CONFIG(tooltip)
        self.wholeWordsCheck.setText(QCoreApplication.translate("TextFinder", u"&Whole Words", None))
#if QT_CONFIG(tooltip)
        self.caseSensitiveCheck.setToolTip(QCoreApplication.translate("TextFinder", u"Make search case sensitive", None))
#endif // QT_CONFIG(tooltip)
        self.caseSensitiveCheck.setText(QCoreApplication.translate("TextFinder", u"&Case Sensitive", None))
        self.findButton.setText(QCoreApplication.translate("TextFinder", u"&Find", None))
#if QT_CONFIG(tooltip)
        self.openButton.setToolTip(QCoreApplication.translate("TextFinder", u"Open another file", None))
#endif // QT_CONFIG(tooltip)
        self.openButton.setText(QCoreApplication.translate("TextFinder", u"&Open...", None))
    # retranslateUi

