import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap, QPalette #调色板
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUi()

    def initUi(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签<font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue) #设置背景色
        label1.setPalette(palette)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setPixmap(QPixmap("../Images/Avatar.jpg"))
        label3.setToolTip("这是一个图片标签")

        label4.setText("<a href='https://www.xl520ld.top'>点击搜索 </a>")
        label4.setOpenExternalLinks(True)
        label4.setAlignment(Qt.AlignCenter)
        label4.setToolTip("这是一个网页链接")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)

    def linkHovered(self):
        print("鼠标滑过label2")

    def linkClicked(self):
        print("鼠标单击label4")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QLabelDemo()
    w.show()

    sys.exit(app.exec_())







