from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtWidgets import QApplication
import sys
import time


class Sound:
    def __init__(self):
        self.sound = QtMultimedia.QSoundEffect()

    def sound_ok(self):
        self.sound.setSource(QtCore.QUrl.fromLocalFile("sound/beep-01a2.wav"))
        self.sound.setVolume(50)
        self.sound.play()

    def sound_ko(self):
        self.sound.setSource(QtCore.QUrl.fromLocalFile("sound/beep-03.wav"))
        self.sound.setVolume(50)
        self.sound.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sound = Sound()
    sound.sound_ok()
    app.exec()
    sys.exit(app.exec())

