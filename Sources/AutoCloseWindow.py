import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel("窗口5秒自动关闭")
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()

    QTimer.singleShot(5000,app.exit)

    sys.exit(app.exec_())