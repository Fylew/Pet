from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import hashlib


text = ["`1234567890-=+_)(*&^%$#@!qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>?"]
class App(QWidget):
    def __init__(self):
        self.start()
        self.Button()


    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()

    def encode(self):
        hash = self.main_menu.textEdit.toPlainText()
        if self.main_menu.comboBox.currentText() == "sha256":
            key = hashlib.sha256(hash.encode('utf-8')).hexdigest()
        elif self.main_menu.comboBox.currentText() == "sha512":
            key = hashlib.sha512(hash.encode('utf-8')).hexdigest()
        elif self.main_menu.comboBox.currentText() == "sha384":
            key = hashlib.sha384(hash.encode('utf-8')).hexdigest()
        elif self.main_menu.comboBox.currentText() == "sha1":
            key = hashlib.sha1(hash.encode('utf-8')).hexdigest()
        elif self.main_menu.comboBox.currentText() == "sha224":
            key = hashlib.sha224(hash.encode('utf-8')).hexdigest()
        elif self.main_menu.comboBox.currentText() == "sha3_384":
            key = hashlib.sha3_384(hash.encode('utf-8')).hexdigest()
        elif self.main_menu.comboBox.currentText() == "sha3_224":
            key = hashlib.sha3_224(hash.encode('utf-8')).hexdigest()
        elif self.main_menu.comboBox.currentText() == "md5":
            key = hashlib.md5(hash.encode('utf-8')).hexdigest()

        self.main_menu.textBrowser_2.setText(f"{key}")


    def decode(self):
        hash = self.main_menu.textEdit.toPlainText()  # мне нужно получить исходный хеш и потом кодировать слова под этот хеш
                                                    # и когда я получу соответсвите по хешам это и будет наш пароль

        while True:
            key = ''
            for i in text:
                if self.main_menu.comboBox_2.currentText() == "sha256":
                    k = hashlib.sha256(key.encode('utf-8')).hexdigest()
                elif self.main_menu.comboBox_2.currentText() == "sha512":
                    k = hashlib.sha512(key.encode('utf-8')).hexdigest()
                elif self.main_menu.comboBox_2.currentText() == "sha384":
                    k = hashlib.sha384(key.encode('utf-8')).hexdigest()
                elif self.main_menu.comboBox_2.currentText() == "sha1":
                    k = hashlib.sha1(key.encode('utf-8')).hexdigest()
                elif self.main_menu.comboBox_2.currentText() == "sha224":
                    k = hashlib.sha224(key.encode('utf-8')).hexdigest()
                elif self.main_menu.comboBox_2.currentText() == "sha3_384":
                    k = hashlib.sha3_384(key.encode('utf-8')).hexdigest()
                elif self.main_menu.comboBox_2.currentText() == "sha3_224":
                    k = hashlib.sha3_224(key.encode('utf-8')).hexdigest()
                elif self.main_menu.comboBox_2.currentText() == "md5":
                    k = hashlib.md5(key.encode('utf-8')).hexdigest()

            if k == hash:
                self.main_menu.textBrowser_3.setText(f"{key}")
                break
            else:
                self.main_menu.textBrowser_3.setText(f"Скоро тут будет ваш пароль)")


    def Button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.encode())
        self.main_menu.pushButton_2.clicked.connect(lambda: self.decode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()