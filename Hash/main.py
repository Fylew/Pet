from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import hashlib
import itertools
import math
import time
from tqdm import tqdm
import random
text = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

def d(hash_form,hash,text):
    h = hashlib.new(hash_form)
    k = hash
    for i in range(1, len(text)):
        for g in tqdm(itertools.combinations("".join(random.sample(text, len(text))), i)):
            if k == h.update(b"{g}") :
                print(g)
                break
        text *= i


class App(QWidget):
    def __init__(self):
        self.start()
        self.Button()


    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()

    def encode(self):
        h = hashlib.new(self.main_menu.comboBox.currentText())
        h.update(b"self.main_menu.textEdit.toPlainText()")
        self.main_menu.textBrowser_2.setText(h.hexdigest())


    def decode(self):
        hash = self.main_menu.textEdit_2.toPlainText()
        hash_form = self.main_menu.comboBox_2.currentText()
        d(hash_form,hash,text)


    def Button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.encode())
        self.main_menu.pushButton_2.clicked.connect(lambda: self.decode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()