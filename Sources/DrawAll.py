import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300, 600)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(Qt.blue))

        #绘制弧0-120度弧
        rect = QRect(0,10,100,100)
        #alen为1/16度
        painter.drawArc(rect,0,120 * 16)

        #带弦的弧
        painter.drawChord(10,120,100,100,90*16,192 * 16)

        #绘制扇形
        painter.drawPie(120,0,100,100,0,115*16)

        #绘制椭圆
        painter.drawEllipse(120,120,100,100)

        #绘制多边形
        point1 = QPoint(140, 380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)

        polygon = QPolygon([point1,point2,point3,point4,point5])
        painter.drawPolygon(polygon)

        #绘制图像
        image = QImage('../Images/Avatar.jpg')
        rect = QRect(10,400, image.width(), image.height())
        painter.drawImage(rect,image)

        painter.end()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DrawAll()
    w.show()
    sys.exit(app.exec_())