import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyTypeSingal(QObject):

    sendMsg = pyqtSignal(object)
    def run(self):
        self.sendMsg.emit("Hello  PyQt5!")

class MySlot(QObject):
    def get(self,msg):
        print(msg)

if __name__ == '__main__':
    send = MyTypeSingal()
    slot = MySlot()

    send.sendMsg.connect(slot.get)

    send.run()
