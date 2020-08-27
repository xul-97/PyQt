import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('文本输入框校验器')

        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()


        formLayout.addRow("整数类型", intLineEdit)
        formLayout.addRow("浮点类型", doubleLineEdit)
        formLayout.addRow("数字和字母", validatorLineEdit)

        #文本框提示内容
        intLineEdit.setPlaceholderText('整数类型')
        doubleLineEdit.setPlaceholderText('浮点类型')
        validatorLineEdit.setPlaceholderText('数字和字母')

        #整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)

        #浮点数校验器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-180, 180)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)#小数位数

        #字符和数字
        reg = QRegExp('^[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QLineEditValidator()
    w.show()

    sys.exit(app.exec_())
