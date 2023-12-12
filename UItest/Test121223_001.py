import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("UI_test001.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("연습 프로그램 1.0")
        self.setWindowIcon(QIcon("..\icon\google.png"))

        self.pushButton.clicked.connect(self.btnClick)
        self.pushButton_2.clicked.connect(self.btnClick_2)

    def btnClick(self):
        self.textEdit.setText("안녕하세요")

    def btnClick_2(self):
        self.textEdit.clear()

app = QApplication(sys.argv)
myProgram = MyWindow()
myProgram.show()
app.exec_()
