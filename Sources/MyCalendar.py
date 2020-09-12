import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QDialog):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1996,1,1))
        self.cal.setMaximumDate(QDate(2030,12,31))
        self.cal.setGridVisible(True)

        self.cal.move(20,20)
        self.resize(400,300)
        self.setWindowTitle("日历演示")

        self.cal.clicked.connect(self.showDate)
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(20,300)

    def showDate(self):
        self.label.setText(self.cal.selectedDate().toString('yyyy-MM-dd dddd'))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyCalendar()
    w.show()
    sys.exit(app.exec_())







