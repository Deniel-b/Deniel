import sys

from PySide2.QtWidgets import QApplication
from PyQT.MainWindow import MainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MainWindow()
    w.resize(1280, 720)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())