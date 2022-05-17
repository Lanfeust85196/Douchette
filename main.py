import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtGui import QKeyEvent
from PyQt5 import Qt


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # création du champ de texte
        self.champ = QLineEdit()
        self.champ.installEventFilter(self)

        # création du bouton
        self.bouton = QPushButton("COPIE")
        # on connecte le signal "clicked" à la méthode "appui_bouton_copie"
        self.bouton.clicked.connect(self.appui_bouton_copie)

        # création de l'étiquette
        self.label = QLabel()

        # mise en place du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.champ)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setWindowTitle("Ma fenetre")

    # on définit une méthode à connecter au signal envoyé
    def appui_bouton_copie(self):
        # la méthode "text" de QLineEdit permet d'obtenir le texte à copier
        texte_a_copier = self.champ.text()
        # la méthode "setText" de QLabel permet de changer
        # le texte de l'étiquette
        self.label.setText(texte_a_copier)

    # définition d'un filtre d'évènement sur le champ text pour récupérer le "Enter"
    def eventFilter(self, obj, event):
        print(event.type() == QEvent.KeyPress)
        if event.type() == QEvent.KeyPress:
            keyevent = QKeyEvent(event)
            print(keyevent.key())
            if keyevent.key() == Qt.Key_Enter:
                # Special tab handling
                return True
            else:
                return False

        return False


app = QApplication.instance()

if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()

app.exec_()
