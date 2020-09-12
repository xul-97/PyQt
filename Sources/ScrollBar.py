import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ScrollBar(QWidget):
    def __init__(self):
        super(ScrollBar, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        self.label = QLabel("拖动滚动条改变颜色")

        hbox.addWidget(self.label)

        self.scrolbar1 = QScrollBar()
        self.scrolbar1.setMaximum(255)
        self.scrolbar1.sliderMoved.connect(self.sliderMoved)

        self.scrolbar2 = QScrollBar()
        self.scrolbar2.setMaximum(255)
        self.scrolbar2.sliderMoved.connect(self.sliderMoved)

        self.scrolbar3 = QScrollBar()
        self.scrolbar3.setMaximum(255)
        self.scrolbar3.sliderMoved.connect(self.sliderMoved)

        self.scrolbar4 = QScrollBar()
        self.scrolbar4.setMaximum(255)
        self.scrolbar4.sliderMoved.connect(self.sliderMoved1)

        hbox.addWidget(self.scrolbar1)
        hbox.addWidget(self.scrolbar2)
        hbox.addWidget(self.scrolbar3)
        hbox.addWidget(self.scrolbar4)

        self.setGeometry(300,300,300,300)
        self.setLayout(hbox)

        self.y = self.label.pos().y()

    def sliderMoved(self):
        print(self.scrolbar1.value(),self.scrolbar2.value(),self.scrolbar3.value())
        palette = QPalette()
        c = QColor(self.scrolbar1.value(),self.scrolbar2.value(),self.scrolbar3.value(), 255)
        palette.setColor(QPalette.Foreground,c)
        self.label.setPalette(palette)

    def sliderMoved1(self):
        self.label.move(self.label.x(),self.y + self.scrolbar4.value())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ScrollBar()
    w.show()
    sys.exit(app.exec_())