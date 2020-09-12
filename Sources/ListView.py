from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class TableView(QWidget):
    def __init__(self, arg =None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle("QListView表格视图控件")
        self.resize(500,300)

        listView = QListView()
        listModel = QStringListModel()

        self.list = ['列表项1', '列表项2', '列表项3']

        listModel.setStringList(self.list)
        listView.setModel(listModel)
        listView.clicked.connect(self.clicked)

        layout = QVBoxLayout()
        layout.addWidget(listView)

        self.setLayout(layout)



    def clicked(self, item):
        QMessageBox.information(self, "QListView", "您选择：" + self.list[item.row()])



if __name__=="__main__":
    app = QApplication(sys.argv)

    w = TableView()
    w.show()

    sys.exit(app.exec_())