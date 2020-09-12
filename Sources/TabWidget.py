import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TabWidget(QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.setWindowTitle("选项卡页面")

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, '选项卡一')
        self.addTab(self.tab2, '选项卡二')
        self.addTab(self.tab3, '选项卡三')

        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址', QLineEdit())

        self.setTabText(0,"Information")
        self.tab1.setLayout(layout)


    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())
        layout.addRow('电话', QLineEdit())

        self.setTabText(1,"信息")
        self.tab2.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = TabWidget()
    w.show()
    sys.exit(app.exec_())