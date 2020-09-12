import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class stackedWidget(QWidget):
    def __init__(self):
        super(stackedWidget, self).__init__()
        self.setWindowTitle("堆栈窗口控件")

        self.list = QListWidget()
        self.list.insertItem(0,'联系方式')
        self.list.insertItem(1,'个人信息')
        self.list.insertItem(2,'教育程度')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.tab1UI()
        self.tab2UI()
        #self.tab3UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hBox = QHBoxLayout()
        hBox.addWidget(self.list)
        hBox.addWidget(self.stack)
        self.setLayout(hBox)

        self.list.currentRowChanged.connect(self.display)

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址', QLineEdit())

        self.stack1.setLayout(layout)


    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())
        layout.addRow('电话', QLineEdit())

        self.stack2.setLayout(layout)

    def display(self,index):
        print(index)
        self.stack.setCurrentIndex(index)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = stackedWidget()
    w.show()
    sys.exit(app.exec_())