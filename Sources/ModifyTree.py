import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree, self).__init__()
        self.setWindowTitle("修改树控件节点")

        self.tree = QTreeWidget()
        # 指定列数
        self.tree.setColumnCount(2)

        # 指定列标签
        self.tree.setHeaderLabels(['key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setIcon(0, QIcon('../Images/icon.ico'))
        self.tree.setColumnWidth(0, 120)

        # 添加子节点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点数据')
        child1.setIcon(0, QIcon('../Images/icon.ico'))
        child1.setCheckState(0, Qt.Checked)

        # 添加子节点
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setText(1, '子节点数据')
        child2.setIcon(0, QIcon('../Images/icon.ico'))

        # 添加子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点3')
        child3.setText(1, '子节点数据')
        child3.setIcon(0, QIcon('../Images/icon.ico'))

        self.tree.clicked.connect(self.onTreeClicked)


        operatorLayout = QHBoxLayout()
        addBtn = QPushButton("添加节点")
        updateBtn = QPushButton("修改节点")
        delteBtn = QPushButton("删除节点")

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(delteBtn)

        addBtn.clicked.connect(self.addNote)
        updateBtn.clicked.connect(self.updateNote)
        delteBtn.clicked.connect(self.deleteNote)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)

        self.setLayout(mainLayout)


    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s, value=%s' % (item.text(0), item.text(1)))


    def addNote(self):
        print("添加节点")
        item = self.tree.currentItem()
        print(item)

        node = QTreeWidgetItem(item)
        node.setText(0,"xinjiedian")
        node.setText(1,"📃")
        pass

    def updateNote(self):
        print("修改节点")
        item = self.tree.currentItem()
        item.setText(0,"修改节点")
        item.setText(1,"值被修改")

        pass

    def deleteNote(self):
        print("删除节点")
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in  self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = ModifyTree()
    w.show()
    sys.exit(app.exec_())