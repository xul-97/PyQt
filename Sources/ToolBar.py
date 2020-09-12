import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(400,200)

        tb1 = self.addToolBar("File")
        new = QAction(QIcon("../Images/Avatar.jpg"),"new",self)
        tb1.addAction(new)

        tb1.setToolButtonStyle(Qt.ToolButtonFollowStyle)#设置图标与文本显示方式


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ToolBar()
    w.show()
    sys.exit(app.exec_())







