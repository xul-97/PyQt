import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()

        self.textCopyButton = QPushButton("复制文本")
        self.textPasteButton = QPushButton("粘贴文本")
        self.htmlCopyButton = QPushButton("复制HTML")
        self.htmlPasteButton = QPushButton("粘贴HTML")
        self.imageCopyButton = QPushButton("复制图像")
        self.imagePasteButton = QPushButton("粘贴图像")

        self.textLabel = QLabel("默认文本")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap('../Images/Avatar.jpg'))

        layout = QGridLayout()
        layout.addWidget(self.textCopyButton,0,0)
        layout.addWidget(self.imageCopyButton,0,1)
        layout.addWidget(self.htmlCopyButton,0,2)
        layout.addWidget(self.textPasteButton, 1, 0)
        layout.addWidget(self.imagePasteButton, 1, 1)
        layout.addWidget(self.htmlPasteButton, 1, 2)

        layout.addWidget(self.textLabel,2,0,1,2)
        layout.addWidget(self.imageLabel,2,2)
        self.setLayout(layout)

        self.textCopyButton.clicked.connect(self.copyText)
        self.textPasteButton.clicked.connect(self.pasteText)
        self.htmlCopyButton.clicked.connect(self.copyHTML)
        self.htmlPasteButton.clicked.connect(self.pasteHTML)
        self.imageCopyButton.clicked.connect(self.copyImage)
        self.imagePasteButton.clicked.connect(self.pasteImage)

    def copyText(self):
        clipBorad = QApplication.clipboard()
        clipBorad.setText('hello world')
    def pasteText(self):
        clipBorad = QApplication.clipboard()
        self.textLabel.setText(clipBorad.text())

    def copyHTML(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipBorad = QApplication.clipboard()
        clipBorad.setMimeData(mimeData)
    def pasteHTML(self):
        clipBorad = QApplication.clipboard()
        mimeData = clipBorad.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

    def copyImage(self):
        clipBorad = QApplication.clipboard()
        clipBorad.setPixmap(QPixmap('../Images/Avatar.jpg'))
    def pasteImage(self):
        clipBorad = QApplication.clipboard()
        self.imageLabel.setPixmap(clipBorad.pixmap())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ClipBoard()
    w.show()
    sys.exit(app.exec_())







