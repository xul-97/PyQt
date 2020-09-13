import sys, math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Splitetr(QWidget):
    def __init__(self):
        super(Splitetr, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle("QSplitter例子")

        self.setGeometry(300,300,300,300)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textEdit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textEdit)


        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Splitetr()
    w.show()
    sys.exit(app.exec_())