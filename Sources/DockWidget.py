import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DockWidget(QMainWindow):
    def __init__(self):
        super(DockWidget, self).__init__()
        self.setWindowTitle("停靠控件")

        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable', self)
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QLineEdit())

        # self.items.setFloating(True)

        self.addDockWidget(Qt.RightDockWidgetArea,self.items)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = DockWidget()
    w.show()
    sys.exit(app.exec_())