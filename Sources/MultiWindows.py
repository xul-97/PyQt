import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MultiWindows(QMainWindow):
    count = 0
    def __init__(self):
        super(MultiWindows, self).__init__()
        self.setWindowTitle("容纳多文档窗口（一个窗口含有多个子窗口）")

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")

        file.triggered.connect(self.windowAction)

    def windowAction(self, q):

        if q.text() == "New":
            MultiWindows.count = MultiWindows.count + 1

            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MultiWindows()
    w.show()
    sys.exit(app.exec_())