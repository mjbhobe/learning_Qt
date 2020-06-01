# byteConverter.py: class to convert 
import sys
from PyQt5.QtCore import *

class ByteConverter(QObject):
    """
    conversions class
    """
    def __init__(self):
        super(ByteConverter, self).__init__()
        self.sigDecChanged = pyqtSignal(str)
        self.sigHexChanged = pyqtSignal(str)
        self.sigBinChanged = pyqtSignal(str)

    @pyqtSlot(str)
    def setDec(decStr):
        # NOTE: decStr is string rep of deciman num
        decNum = int(decStr, base=10)
        emit sigHexChanged(hex(decNum))
        emit sigBinChanged(bin(decNum))