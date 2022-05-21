from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5 import QtCore
from LabelEdit import LabelEdit


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(100, 100, 600, 400)

        # Label creation site
        self.label = QLabel()
        self.label.setGeometry(200, 150, 100, 50)
        self.label.setStyleSheet("border : 1px solid black;")
        self.label.setAlignment(QtCore.Qt.AlignTop)

        # field Text creation
        self.champ = LabelEdit(self.label)

        # Layout creation
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.champ)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.setWindowTitle("Inventaire ISIAC")
