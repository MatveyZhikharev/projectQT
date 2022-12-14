import sys
from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPolygonF, QPainterPath


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        rand_x = randint(10, 100)
        rand_y = randint(10, 100)
        if status == 1:
            self.qp.drawEllipse(*self.coords_, rand_x, rand_y)
        elif status == 2:
            self.qp.drawRect(*self.coords_, rand_x, rand_y)
        elif status == 3:
            x, y = self.coords_
            R = rand_x
            a = rand_y
            coords = [(x, y + R), (x + a, y - R), (x - a, y - R)]
            self.path = QPainterPath()
            self.path.moveTo(*coords[0])
            self.path.lineTo(*coords[1])
            self.path.lineTo(*coords[2])
            self.path.lineTo(*coords[0])
            self.qp.fillPath(self.path, QColor(randint(0, 255),
                                               randint(0, 255),
                                               randint(0, 255)))

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Рисование')

        self.show()

    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        if (event.button() == Qt.LeftButton):
            self.status = 1
        elif (event.button() == Qt.RightButton):
            self.status = 2
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())