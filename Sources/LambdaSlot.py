from PyQt5.QtWidgets import *
import sys
from functools import partial

class LambdaSlot(QMainWindow):
    def __init__(self):
        super(LambdaSlot, self).__init__()
        self.setWindowTitle("使用Lambda表达式")

        button1 = QPushButton("按钮1")
        button2 = QPushButton("按钮2")

        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        button2.clicked.connect(partial(self.onButtonClick,30,50))

        button1.clicked.connect(lambda :self.onButtonClick(10,20))

    def onButtonClick(self,m,n):
        print("m + n =", m + n)
        QMessageBox.information(self,'结果',str(m+n))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LambdaSlot()
    w.show()
    sys.exit(app.exec_()),