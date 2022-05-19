from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QKeyEvent
from Database import Database
from Log import slogger


class LabelEdit(QLineEdit):
    def __init__(self):
        QLineEdit.__init__(self)
        self.installEventFilter(self)
        slogger(f"Fin __Init__", __name__)

    # Event filter on Text
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            keyevent = QKeyEvent(event)
            if keyevent.key() == Qt.Key_Enter or keyevent.key() == Qt.Key_Return:
                data = Database()
                data.connect()
                if data.find_site(self.text()):
                    slogger(f"eventFilter=>Site OK", __name__)
                else:
                    data.insert_site(self.text(), self.text())
                    slogger(f"eventFilter=>Insert new site", __name__)
                data.close()
                self.setText("")
                slogger(f"Fin eventFilter True", __name__)
                return True
            else:
                slogger(f"Fin eventFilter False", __name__)
                return False
            slogger(f"Fin eventFilter False", __name__)
        return False
