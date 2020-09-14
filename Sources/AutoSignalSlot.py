import sys
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okBtn = QPushButton("ok", self)
        self.okBtn.setObjectName("okBtn")

        layout = QHBoxLayout()
        layout.addWidget(self.okBtn)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)
        #self.okBtn.clicked.connect(self.on_okButton_clicked)

    @QtCore.pyqtSlot()
    def on_okBtn_clicked(self): #自动绑定信号与槽时，槽函数命名必须为on_对象名_信号名
        print("点击了ok按钮")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AutoSignalSlot()
    w.show()
    sys.exit(app.exec_())