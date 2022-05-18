from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QKeyEvent


class LabelEdit(QLineEdit):
    def __init__(self):
        QLineEdit.__init__(self)

        self.installEventFilter(self)

    # Event filter on Text
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            keyevent = QKeyEvent(event)
            if keyevent.key() == Qt.Key_Enter or keyevent.key() == Qt.Key_Return:
                print(self.text())
                self.setText("")
                return True
            else:
                return False

        return False
