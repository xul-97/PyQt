import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BasicTreeWidegt(QMainWindow):
    def __init__(self, parent=None):
        super(BasicTreeWidegt, self).__init__(parent)

        self.setWindowTitle("树控件")
        self.tree = QTreeWidget()
        #指定列数
        self.tree.setColumnCount(2)

        #指定列标签
        self.tree.setHeaderLabels(['key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('../Images/icon.ico'))
        self.tree.setColumnWidth(0,120)

        #添加子节点
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点数据')
        child1.setIcon(0,QIcon('../Images/icon.ico'))
        child1.setCheckState(0,Qt.Checked)

        # 添加子节点
        child2 = QTreeWidgetItem(child1)
        child2.setText(0, '子节点2')
        child2.setText(1, '子节点数据')
        child2.setIcon(0, QIcon('../Images/icon.ico'))

        self.tree.clicked.connect(self.onTreeClicked)
        self.setCentralWidget(self.tree)
    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s, value=%s' % (item.text(0),item.text(1)))

if __name__=="__main__":
    app = QApplication(sys.argv)

    w = BasicTreeWidegt()
    w.show()

    sys.exit(app.exec_())