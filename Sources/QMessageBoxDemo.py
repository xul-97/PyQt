import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QMessageBoxDemo案例")
        self.resize(300,200)

        layout = QVBoxLayout()
        self.button = QPushButton()
        self.button.setText("显示关于对话框")
        self.button.clicked.connect(self.showDialog)

        self.button1 = QPushButton()
        self.button1.setText("显示消息对话框")
        self.button1.clicked.connect(self.showDialog)

        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == "显示关于对话框":
            QMessageBox.about(self,'关于', '这是一个关于对话框')
        if text == "显示消息对话框":
            QMessageBox.information(self,'消息', '这是一个消息对话框')

if __name__=='__main__':
    app = QApplication(sys.argv)

    w = QMessageBoxDemo()
    w.show()

    sys.exit(app.exec_())