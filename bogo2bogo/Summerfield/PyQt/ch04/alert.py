#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* alert.py - hybrid command line & GUI app that displays alert/alarm at
*   a specified hh:mm time
*   usage: python alert.py HH:MM [optional message]
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp


def main():
    try:
        app = PyQtApp(sys.argv)

        # alert.py HH:mm [optional message]
        due = QTime.currentTime()
        message = "Alert!"
        if len(sys.argv) < 2:
            raise ValueError
        hours, mins = sys.argv[1].split(":")
        due = QTime(int(hours), int(mins))
        if not due.isValid():
            raise ValueError
        # parse optional message
        if len(sys.argv) > 2:
            message = " ".join(sys.argv[2:])

        # wait until it's due time
        while QTime.currentTime() < due:
            time.sleep(20)
        label = QLabel(f"<html><font color='red' size=32>{message}</font></html>")
        label.setWindowFlags(Qt.SplashScreen)
        label.show()
        QTimer.singleShot(10000, app.quit)
        return app.exec()
    except ValueError:
        print("Usage: python alert.py HH:mm [optional message]")


if __name__ == "__main__":
    main()
