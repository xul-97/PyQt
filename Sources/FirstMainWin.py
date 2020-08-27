# This is a sample Python script for practicing PyQt.
# Author: xuliang
import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        self.setWindowTitle("第一个主窗口")
        self.resize(400,300)
        self.setWindowIcon(QIcon("../Images/icon.ico"))

        self.status = self.statusBar()
        self.status.showMessage("只存在5秒消息", 5000)

        #添加按钮
        self.button = QPushButton('退出应用程序')
        self.button.clicked.connect(self.clickEvent)

        #控件添加鼠标停留提示
        QToolTip.setFont(QFont('SanaSerif',9))
        self.button.setToolTip("这是个按钮")

        #添加布局
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        #添加容器
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        #设置中心窗口
        self.setCentralWidget(mainFrame)

        self.centerWin()

    def centerWin(self):
        #获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标
        size = self.geometry()

        left = (screen.width() - self.width()) / 2
        top = (screen.height() - self.height()) / 2

        self.move(left, top)

    def clickEvent(self):
        app.instance()
        app.exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = FirstMainWin()
    w.show()


    sys.exit(app.exec_())

