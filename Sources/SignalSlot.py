import sys, math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SignalSlot(QWidget):
    def __init__(self):
        super(SignalSlot, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("信号与槽")
        self.setGeometry(300,300,500,400)
        self.btn = QPushButton('我的按钮',self)
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        self.btn.setText("信号发出")
        self.btn.setStyleSheet("QPushButton{max-width:200px; min-width:200px}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SignalSlot()
    w.show()
    sys.exit(app.exec_())