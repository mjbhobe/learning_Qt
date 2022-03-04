"""
* sliders.py: PyQt version of the sliders Qt widgets demo using Chocolaf
* @author (Chocolaf): Manish Bhobe
*
* PyQt demo code taken from https://github.com/baoboa/pyqt5/tree/master/examples/widgets
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[2], 'common_files'))
# from pyqt5_utils import PyQtApp
import chocolaf
from chocolaf.utils.pyqtapp import PyQtApp


class MoviePlayer(QWidget):
    def __init__(self, parent=None):
        super(MoviePlayer, self).__init__(parent)

        self.movie = QMovie(self)
        self.movie.setCacheMode(QMovie.CacheAll)

        self.movieLabel = QLabel("No movie loaded")
        self.movieLabel.setAlignment(Qt.AlignCenter)
        self.movieLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.movieLabel.setBackgroundRole(QPalette.Dark)
        self.movieLabel.setAutoFillBackground(True)

        self.currentMovieDirectory = ''

        self.createControls()
        self.createButtons()

        self.movie.frameChanged.connect(self.updateFrameSlider)
        self.movie.stateChanged.connect(self.updateButtons)
        self.fitCheckBox.clicked.connect(self.fitToWindow)
        self.frameSlider.valueChanged.connect(self.goToFrame)
        self.speedSpinBox.valueChanged.connect(self.movie.setSpeed)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.movieLabel)
        mainLayout.addLayout(self.controlsLayout)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)

        self.updateFrameSlider()
        self.updateButtons()

        self.setWindowTitle("Movie Player")
        self.resize(400, 400)

    def open(self):
        videosPath = QStandardPaths.standardLocations(QStandardPaths.MoviesLocation)
        fileName, _ = QFileDialog.getOpenFileName(self, "Open a Movie", videosPath[-1],
                                                  self.currentMovieDirectory)

        if fileName:
            self.openFile(fileName)

    def openFile(self, fileName):
        self.currentMovieDirectory = QFileInfo(fileName).path()

        self.movie.stop()
        self.movieLabel.setMovie(self.movie)
        self.movie.setFileName(fileName)
        self.movie.start()

        self.updateFrameSlider()
        self.updateButtons()

    def goToFrame(self, frame):
        self.movie.jumpToFrame(frame)

    def fitToWindow(self):
        self.movieLabel.setScaledContents(self.fitCheckBox.isChecked())

    def updateFrameSlider(self):
        hasFrames = (self.movie.currentFrameNumber() >= 0)

        if hasFrames:
            if self.movie.frameCount() > 0:
                self.frameSlider.setMaximum(self.movie.frameCount() - 1)
            elif self.movie.currentFrameNumber() > self.frameSlider.maximum():
                self.frameSlider.setMaximum(self.movie.currentFrameNumber())

            self.frameSlider.setValue(self.movie.currentFrameNumber())
        else:
            self.frameSlider.setMaximum(0)

        self.frameLabel.setEnabled(hasFrames)
        self.frameSlider.setEnabled(hasFrames)

    def updateButtons(self):
        state = self.movie.state()

        self.playButton.setEnabled(self.movie.isValid() and
                                   self.movie.frameCount() != 1 and state == QMovie.NotRunning)
        self.pauseButton.setEnabled(state != QMovie.NotRunning)
        self.pauseButton.setChecked(state == QMovie.Paused)
        self.stopButton.setEnabled(state != QMovie.NotRunning)

    def createControls(self):
        self.fitCheckBox = QCheckBox("Fit to Window")

        self.frameLabel = QLabel("Current frame:")

        self.frameSlider = QSlider(Qt.Horizontal)
        self.frameSlider.setTickPosition(QSlider.TicksBelow)
        self.frameSlider.setTickInterval(10)

        speedLabel = QLabel("Speed:")

        self.speedSpinBox = QSpinBox()
        self.speedSpinBox.setRange(1, 9999)
        self.speedSpinBox.setValue(100)
        self.speedSpinBox.setSuffix("%")

        self.controlsLayout = QGridLayout()
        self.controlsLayout.addWidget(self.fitCheckBox, 0, 0, 1, 2)
        self.controlsLayout.addWidget(self.frameLabel, 1, 0)
        self.controlsLayout.addWidget(self.frameSlider, 1, 1, 1, 2)
        self.controlsLayout.addWidget(speedLabel, 2, 0)
        self.controlsLayout.addWidget(self.speedSpinBox, 2, 1)

    def createButtons(self):
        iconSize = QSize(36, 36)

        openButton = QToolButton()
        openButton.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        openButton.setIconSize(iconSize)
        openButton.setToolTip("Open File")
        openButton.clicked.connect(self.open)

        self.playButton = QToolButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.setIconSize(iconSize)
        self.playButton.setToolTip("Play")
        self.playButton.clicked.connect(self.movie.start)

        self.pauseButton = QToolButton()
        self.pauseButton.setCheckable(True)
        self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.pauseButton.setIconSize(iconSize)
        self.pauseButton.setToolTip("Pause")
        self.pauseButton.clicked.connect(self.movie.setPaused)

        self.stopButton = QToolButton()
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.setIconSize(iconSize)
        self.stopButton.setToolTip("Stop")
        self.stopButton.clicked.connect(self.movie.stop)

        quitButton = QToolButton()
        quitButton.setIcon(self.style().standardIcon(QStyle.SP_DialogCloseButton))
        quitButton.setIconSize(iconSize)
        quitButton.setToolTip("Quit")
        quitButton.clicked.connect(self.close)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(openButton)
        self.buttonsLayout.addWidget(self.playButton)
        self.buttonsLayout.addWidget(self.pauseButton)
        self.buttonsLayout.addWidget(self.stopButton)
        self.buttonsLayout.addWidget(quitButton)
        self.buttonsLayout.addStretch()


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = PyQtApp(sys.argv)
    app.setStyle("QDarkStyle-dark")

    win = MoviePlayer()
    # win.setStyleSheet(app.getStyleSheet("Chocolaf"))
    win.move(50, 50)
    win.show()

    return app.exec()


if __name__ == "__main__":
    main()
