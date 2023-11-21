from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import random
import json

file = open('lib_word.json',"r",encoding='utf-8')
data = json.load(file)

off_list = []
letter_get = ""
count = 0
class App(QWidget):
    def __init__(self):
        self.start()
        self.button()
        self.main_menu.pushButton_2.hide()
    def start(self):
        self.main_menu = uic.loadUi("mainmenu.ui")
        self.main_menu.show()

    def com_choice(self):
        global letter_get,data
        word = random.choice(data[letter_get.upper()])
        if word not in off_list:
            if word[-1] == "ь" or word[-1] == "ъ":
                self.main_menu.textBrowser.setText(f'Мое слово {word}\nТебе на {word[-2]}')
                letter_get = word[-2]
            else:
                self.main_menu.textBrowser.setText(f'Мое слово {word}\nТебе на {word[-1]}')
                letter_get = word[-1]


    def go(self):
        global letter_get,off_list,count
        if self.main_menu.textEdit.toPlainText()[-1] == "ь" or self.main_menu.textEdit.toPlainText()[-1] == "ъ":
            off_list.append(self.main_menu.textEdit.toPlainText())
            letter_get = self.main_menu.textEdit.toPlainText()[-2]
            self.com_choice()
            count += 1
            self.main_menu.textBrowser_2.setText(f"Кол-во введенных слов - {count}")
        else:
            if self.main_menu.textEdit.toPlainText() in off_list:
                self.main_menu.textBrowser.setText("Ей, это слово уже было!")
            else:
                if len(self.main_menu.textEdit.toPlainText()) < 1:
                    self.main_menu.textBrowser.setText(f'{random.choice(["Мне кажется ты что-то забыл","Введи слово","Ты что буквы забыл?"])}')
                else:
                    if self.main_menu.textEdit.toPlainText()[0] != letter_get and count != 0:
                        self.main_menu.textBrowser.setText(f'{random.choice([f"Слово должно начаться на букву {letter_get}", f"Ты что читать не умеешь? Тебе на {letter_get}"])}')
                    else:
                        off_list.append(self.main_menu.textEdit.toPlainText())
                        letter_get = self.main_menu.textEdit.toPlainText()[-1]
                        self.com_choice()
                        count += 1
                        self.main_menu.textBrowser_2.setText(f"Кол-во введенных слов - {count}")
        self.main_menu.textEdit.clear()
    def new(self):
        ...
    def button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.go())
        self.main_menu.pushButton_2.clicked.connect(lambda: self.new())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()