import re
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QKeyEvent
from Database import Database
from Log import slogger


class LabelEdit(QLineEdit):
    def __init__(self, label: QLabel):
        slogger(f"__Init__", __name__)
        QLineEdit.__init__(self)
        self.installEventFilter(self)
        self.label = label
        self.data = Database()
        self.site = ""

    # Event filter on Text
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            keyevent = QKeyEvent(event)
            if keyevent.key() == Qt.Key_Enter or keyevent.key() == Qt.Key_Return:
                # Input validation
                x = re.search("^L561[0-9]{8}$", self.text())
                y = re.search("^561[0-9]{8}$", self.text())
                if x:
                    self.data.connect()
                    if self.data.find_site(self.text()):
                        slogger(f"eventFilter=>Site OK : {self.text()}", __name__)
                        self.label.setText(f"site = {self.text()}")
                        self.site = self.text()
                    else:
                        slogger(f"eventFilter=>Insert new site : {self.text()}", __name__)
                        self.label.setText(f"site = {self.text()}")
                        self.site = self.text()
                        self.data.insert_site(self.text(), self.text())
                    self.data.close()
                elif y:
                    if self.site != "":
                        slogger(f"eventFilter=>Insert new Item : {self.text()}", __name__)
                        self.data.connect()
                        if self.data.find_bien(self.site, self.text()):
                            self.label.setText(f"Le bien {self.text()} a déjà été scanné dans ce lieu")
                        else:
                            self.data.insert_bien(self.site, self.text(), self.text())
                            self.label.setText(f"site = {self.site} bien = {self.text()}")
                        self.data.close()
                    else:
                        slogger(f"eventFilter=>No site, can't insert new Item : {self.text()}", __name__)
                        self.label.setText("Pas de site sélectionné")
                else:
                    self.label.setText("Code barre incorrect")
                    slogger(f"eventFilter=>NOK : {self.text()}", __name__)
                self.setText("")
                slogger(f"Fin eventFilter True", __name__)
                return True
            else:
                # slogger(f"Fin eventFilter False", __name__)
                return False
        # slogger(f"Fin eventFilter False", __name__)
        return False
