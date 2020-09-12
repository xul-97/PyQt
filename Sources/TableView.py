from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableView(QWidget):
    def __init__(self, arg =None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle("QTableView表格视图控件")
        self.resize(500,300)

        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])

        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        #添加数据
        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')

        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)

        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)




if __name__=="__main__":
    app = QApplication(sys.argv)

    w = TableView()
    w.show()

    sys.exit(app.exec_())