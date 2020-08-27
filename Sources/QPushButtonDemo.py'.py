import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("按钮实例")

        layout = QVBoxLayout()

        self.button1 = QPushButton("第一个按钮")
        self.button1.setText("First Button")
        self.button1.setCheckable(True)
        self.button1.toggle() #开关特性
        self.button1.clicked.connect(lambda:self.whichBUtton(self.button1))



        self.button2 = QPushButton('&Button')
        #self.button2.setText("图像按钮")
        self.button2.setIcon(QIcon(QPixmap("../Images/icon.ico")))
        self.button2.clicked.connect(lambda:self.whichBUtton(self.button2))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def whichBUtton(self,btn):
        print("单击的按钮为" + btn.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QPushButtonDemo()
    w.show()

    sys.exit(app.exec_())