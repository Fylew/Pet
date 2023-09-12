from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import random
za = ["qwertyuiopasdfghjklzxcvbnm"]
Za = ["QWERTYUIOPASDFGHJKLZXCVBNM"]
number = ["1234567890"]
spec = ["!#$%^&*()_+=-}{[]\|/.,';"]

class App(QWidget):


    def __init__(self):
        self.start()
        self.Button()
    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()

    def info(self,a):
        gen_pass_list = ""
        if self.main_menu.checkBox.isChecked():
            gen_pass_list += za[0]

        if self.main_menu.checkBox_2.isChecked():
            gen_pass_list += Za[0]

        if self.main_menu.checkBox_3.isChecked():
            gen_pass_list += number[0]

        if self.main_menu.checkBox_4.isChecked():
            gen_pass_list += spec[0]

        gen_out = ""
        for i in range(self.main_menu.spinBox.value()):
            gen_out += random.choice(gen_pass_list)

        self.main_menu.textBrowser.setText(f"\t\tВаш пароль\n {gen_out}\n{'='*45}")


    def Button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.info('1'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()