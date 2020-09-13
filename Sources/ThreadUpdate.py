import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)

class ThreadUpdateUi(QDialog):
    def __init__(self):
        super(ThreadUpdateUi, self).__init__()
        self.resize(400,100)
        self.input = QLineEdit(self)
        self.input.resize(400,100)
        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self,data):
        self.input.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ThreadUpdateUi()
    w.show()
    sys.exit(app.exec_())