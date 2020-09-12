import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DateTimeEdit(QDialog):
    def __init__(self):
        super(DateTimeEdit, self).__init__()
        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit2.setCalendarPopup(True)

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')

        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat('HH::mm::ss')

        vLayout.addWidget(dateTimeEdit1)
        vLayout.addWidget(dateTimeEdit2)
        vLayout.addWidget(dateEdit)
        vLayout.addWidget(timeEdit)

        self.setLayout(vLayout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DateTimeEdit()
    w.show()
    sys.exit(app.exec_())







