# sigslog.py: signals & slots
import sys, os
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# using qdarkstyle (@see: https://github.com/ColinDuquesnoy/QDarkStyleSheet)
import qdarkstyle
# to detect dark themes (@see: https://pypi.org/project/darkdetect/)
import darkdetect

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
print(f"PySide plugin path - {plugin_path}")

MIN_C, MAX_C = -100, 100

class SigSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()

    def c2f(self, celcius):
        farenheit = celcius * (9.0/5.0) + 32.0
        return farenheit

    def initGui(self):
        # self.setWindowTitle(f"PyQt {PYQT_VERSION_STR} Temp Converter")
        self.setWindowTitle(f"PySide Temp Converter")
        self.spinner = QSpinBox()
        self.slider = QSlider(Qt.Horizontal)
        self.faren = QLabel("")
        # self.qtVer = QLabel(f"Built with PyQt {PYQT_VERSION_STR}")
        self.qtVer = QLabel(f"Built with PySide {PySide2.__version__}")
        self.quit = QPushButton("Quit!")
        self.quit.setMinimumWidth(100)

        self.quit.setToolTip("Quit application")
        self.spinner.setRange(MIN_C, MAX_C)
        self.slider.setRange(int(self.c2f(MIN_C)), int(self.c2f(MAX_C)))
        self.slider.setEnabled(False)  # so users don't drag it
        # increase min width of slider, so controls are not so scrunched up
        self.slider.setMinimumWidth(300)

        # layput the controls
        widgets = QHBoxLayout()
        widgets.addWidget(self.spinner)
        widgets.addWidget(self.slider)
        widgets.addWidget(self.faren)
        buttons = QHBoxLayout()
        buttons.addWidget(self.qtVer)
        buttons.addStretch()
        buttons.addWidget(self.quit)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(widgets)
        mainLayout.addLayout(buttons)
        self.setLayout(mainLayout)

        # signals & slots
        self.spinner.valueChanged.connect(self.celciusChanged)
        self.quit.clicked.connect(QApplication.instance().quit)

    def celciusChanged(self):
        celciusTemp = self.spinner.value()
        farenTemp = self.c2f(celciusTemp)
        self.slider.setValue(int(farenTemp))
        fVal = f"<html><b>{farenTemp:.2f}&deg;F</b></html>"
        self.faren.setText(fVal)

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    # font = QFont('SF UI Text', 10)
    app.setFont(QApplication.font("QMenu"))
    if darkdetect.isDark():
        # apply dark stylesheet
        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))

    w = SigSlot()
    # trigger the signals & Slots
    w.spinner.setValue(20)
    w.show()

    return app.exec_()

if __name__ == '__main__':
    main()
