import sys
from PyQt5.QtWidgets import *

class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("QLabel伙伴关系")

        namelabel = QLabel('&Name')
        nameLineEdit = QLineEdit(self)
        #设置伙伴关系
        namelabel.setBuddy(nameLineEdit)

        pwlabel = QLabel('&Password')
        pwLineEdit = QLineEdit(self)
        # 设置伙伴关系
        pwlabel.setBuddy(pwLineEdit)

        btnOk = QPushButton('&Ok')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(namelabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)
        mainLayout.addWidget(pwlabel,1,0)
        mainLayout.addWidget(pwLineEdit,1,1,1,2)
        mainLayout.addWidget(btnOk,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QLabelBuddy()
    w.show()

    sys.exit(app.exec_())
