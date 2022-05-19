from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from LabelEdit import LabelEdit


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # field Text creation
        self.champ = LabelEdit()

        # Label creation site
        self.label = QLabel()

        # Layout creation
        layout = QVBoxLayout()
        layout.addWidget(self.champ)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setWindowTitle("Inventaire ISIAC")