import sys
from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication.instance()

    if not app:
        app = QApplication(sys.argv)

    fen = MainWindow()
    fen.show()

    app.exec_()


if __name__ == "__main__":
    main()
