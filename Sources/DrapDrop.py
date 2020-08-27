#让控件支持拖拽

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyComboxBox(QComboBox):
    def __init__(self):
        super(MyComboxBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        print(event)
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        self.addItem(event.mimeData().text())
class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("请将左边文本拖拽到右边下拉列表"))
        lineEdit =QLineEdit()
        lineEdit.setDragEnabled(True)

        combo = MyComboxBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle("拖拽案例")


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = DrapDropDemo()
    w.show()
    sys.exit(app.exec_())