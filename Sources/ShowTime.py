import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class showTime(QWidget):
    def __init__(self):
        super(showTime, self).__init__()
        self.setWindowTitle("多线程显示时间")
        self.label = QLabel("显示当前时间")
        self.startBtn = QPushButton('开始')
        self.stopBtn = QPushButton('结束')
        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.stopBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.stopBtn.clicked.connect(self.stopTimer)

        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss: dddd")
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)
    def stopTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = showTime()
    w.show()
    sys.exit(app.exec_())