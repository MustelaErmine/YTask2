import sys

from random import randint
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class Focus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.newCyrcle = False

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circle)

    def circle(self):
        self.newCyrcle = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.newCyrcle:
            qp.setBrush(QColor(255, 255, 0))
            centerX = randint(0, 480)
            centerY = randint(0, 340)
            r = randint(10, 100)
            qp.drawEllipse(centerX, centerY, r, r)
            self.newCyrcle = False
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    focus = Focus()
    focus.show()
    sys.exit(app.exec())