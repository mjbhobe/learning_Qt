# byteConverterDialog.py: dialog interface, built manually
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CenteredOnDesktopWidget(QWidget):
    """
    custom widget that centers itself on screen when shown
    derive your widget (usually top window) from this widget
    """
    def __init__(self, *args, **kwargs):
        super(CenteredOnDesktopWidget, self).__init__(*args, **kwargs)

    def show(self):
        """
        shows the widget centered on desktop
        """
        super(CenteredOnDesktopWidget,self).show()
        screenSize = QApplication.desktop().screenGeometry()
        left = (screenSize.width() - self.width()) // 2
        top  = (screenSize.height() - self.height()) // 2
        self.move(left, top)

class ByteConverterDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)

        # setup Gui
        self.setWindowTitle("PyQt: Byte Converter")
        
        # build the layout
        # top row - prompt
        self.prompt = QLabel("Type in a decimal number (8 digits max) into\n" +
                             "the decimal field to see hex & binary values")
        # middle - 3 rows of labels + lineedits
        self.decLabel = QLabel("Decimal:")
        self.hexLabel = QLabel("Hex:")
        self.binLabel = QLabel("Binary:")
        self.decEdit = QLineEdit()
        self.hexEdit = QLineEdit()
        self.binEdit = QLineEdit()
        # set validators for line edits
        #self.decValidator = QIntValidator(0, 999, self.decEdit)
        decExpr = QRegExp(r'[0-9]{0,8}') # just 0-255
        self.decValidator = QRegExpValidator(decExpr, self.decEdit)
        self.decEdit.setValidator(self.decValidator)
        hexExpr = QRegExp(r'[0-9a-fA-F]{1,2}') # upto 2 chars only!
        self.hexValidator = QRegExpValidator(hexExpr, self.hexEdit)
        self.hexEdit.setValidator(self.hexValidator)
        binExpr = QRegExp(r'[0-1]{1,8}') # upto 8 chars only!
        self.binValidator = QRegExpValidator(binExpr, self.binEdit)
        self.binEdit.setValidator(self.binValidator)
        # bottom row - hgap - push button
        self.btnQuit = QPushButton("Quit")
        self.btnQuit.setToolTip("Quit Application")

        # to begin with, let's allow editing in ONLY The decEdit
        #self.hexEdit.setReadOnly(True)
        self.setReadOnly(self.hexEdit)
        self.setReadOnly(self.binEdit)

        promptLayout = QHBoxLayout()
        promptLayout.addWidget(self.prompt)

        editLayout = QGridLayout()
        editLayout.addWidget(self.decLabel, 0, 0)
        editLayout.addWidget(self.decEdit, 0, 1)
        editLayout.addWidget(self.hexLabel, 1, 0)
        editLayout.addWidget(self.hexEdit, 1, 1)
        editLayout.addWidget(self.binLabel, 2, 0)
        editLayout.addWidget(self.binEdit, 2, 1)

        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        btnLayout.addWidget(self.btnQuit)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(promptLayout)
        mainLayout.addLayout(editLayout)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)

        # setup signals & slots
        self.decEdit.textChanged.connect(self.decChanged)
        self.hexEdit.textChanged.connect(self.hexChanged)
        #self.binEdit.textChanged.connect(self.binChanged)
        self.btnQuit.clicked.connect(QApplication.instance().quit)

    def decChanged(self):
        # NOTE: since we have applied a validator to decEdit
        # we can be sure that decEdit holds either a blank string or
        # a valid string representation of an integer
        decValue = self.decEdit.text()
        if len(decValue.strip()) != 0:
            numDecValue = int(decValue, base=10)
            self.hexEdit.setText(hex(numDecValue))
            self.binEdit.setText(bin(numDecValue))
        else:
            self.hexEdit.setText("")
            self.binEdit.setText("")

    def hexChanged(self):
        # NOTE: since we have applied a validator to hexEdit
        # we can be sure that it holds either a blank string or
        # a valid string representation of a hex number
        hexValue = self.hexEdit.text()
        if len(hexValue.strip()) != 0:
            numHexValue = int(hexValue, base=16)
            self.decEdit.setText(f"{numHexValue}")
            self.binEdit.setText(bin(numHexValue))
        else:
            self.decEdit.setText("")
            self.binEdit.setText("")

    def setReadOnly(self, lineEdit, mode=True):
        assert type(lineEdit) == type(self.decEdit), "Expecting QLineEdit as arg to setReadOnly"
        # @see: https://stackoverflow.com/questions/23915700/how-to-make-a-qlineedit-not-editable-in-windows
        # we need to set lineEdit to read only & modify the palette as well
        lineEditPalette = lineEdit.palette()
        colorGroup = QPalette.Disabled if mode == True else QPalette.Active
        textColor = lineEditPalette.color(colorGroup, QPalette.WindowText)
        backColor = lineEditPalette.color(colorGroup, QPalette.Base)
        lineEditPalette.setColor(QPalette.Base, backColor)
        lineEditPalette.setColor(QPalette.WindowText, backColor)

        lineEdit.setReadOnly(mode)
        lineEdit.setPalette(lineEditPalette)

def main():
    app = QApplication(sys.argv)

    w = ByteConverterDialog()
    w.decEdit.setText("75")
    w.show()
    return app.exec_()

if __name__ == '__main__':
    main()