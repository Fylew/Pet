from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import math


itog = {'Замок':0,
        "Протектор":0,
        "Кольца":0,
        "Шарик":0,
        "Штрих-код":0,
        "Пакет":0,
        "Цепочка":0,
        "Трос":0,
        "Бусины":0
        }
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.start()
        self.Button()
        self.main_menu.comboBox.currentTextChanged.connect(self.comboBoxChanged)

        self.main_menu.spinBox.setMaximum(1000000)

    def comboBoxChanged(self, text):
        if text == "Лунница":
            self.main_menu.label_6.show()
            self.main_menu.comboBox_2.show()
        elif text == "Круг" or text == "Сердечко":
            self.main_menu.label_6.show()
            self.main_menu.comboBox_2.show()
            self.main_menu.label_7.show()
            self.main_menu.comboBox_3.show()
        else:
            self.main_menu.label_5.hide()
            self.main_menu.label_6.hide()
            self.main_menu.label_7.hide()
            self.main_menu.comboBox_2.hide()
            self.main_menu.comboBox_3.hide()
    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()
        self.main_menu.label_5.hide()
        self.main_menu.label_6.hide()
        self.main_menu.label_7.hide()
        self.main_menu.comboBox_2.hide()
        self.main_menu.comboBox_3.hide()

    def chek(self,s):
        print(s)

    def lun(self,name):
        count = self.main_menu.spinBox.value()
        if name == "Лунница":
            if f"{name+' '+self.main_menu.comboBox_2.currentText()}" not in itog:
                itog[f"{name+' '+self.main_menu.comboBox_2.currentText()}"] = count
            else:
                itog[f"{name+' '+self.main_menu.comboBox_2.currentText()}"] += count

            itog["Бусины"] += 90 * count
            itog["Цепочка"] += 13 * count
            itog["Трос"] += 42 * count
            itog["Кольца"] += 2 * count

        elif name == "Сердечко":
            if f"{name+' '+self.main_menu.comboBox_2.currentText() + ' ' + self.main_menu.comboBox_3.currentText()}" not in itog:
                itog[f"{name+' '+self.main_menu.comboBox_2.currentText() + ' ' + self.main_menu.comboBox_3.currentText()}"] = count
            else:
                itog[f"{name+' '+self.main_menu.comboBox_2.currentText() + ' ' + self.main_menu.comboBox_3.currentText()}"] += count

            itog["Бусины"] += 65 * count
            itog["Цепочка"] += 5 * count
            itog["Трос"] += 42 * count
            itog["Кольца"] += 3 * count

        elif name == "Круг":
            if f"{name+' '+self.main_menu.comboBox_2.currentText() + ' ' + self.main_menu.comboBox_3.currentText()}" not in itog:
                itog[f"{name+' '+self.main_menu.comboBox_2.currentText() + ' ' + self.main_menu.comboBox_3.currentText()}"] = count
            else:
                itog[f"{name+' '+self.main_menu.comboBox_2.currentText() + ' ' + self.main_menu.comboBox_3.currentText()}"] += count

            itog["Бусины"] += 90 * count
            itog["Цепочка"] += 13 * count
            itog["Трос"] += 40 * count
            itog["Кольца"] += 3 * count

        elif name == "Глаз фатимы":
            if name not in itog:
                itog[name] = count
            else:
                itog[name] += count
        elif name == "Шпинель":
            if name not in itog:
                itog[name] = count
            else:
                itog[name] += count
        elif name == "Радужный цветок":
            if name not in itog:
                itog[name] = count
            else:
                itog[name] += count
        elif name == "Браслеты":
            if name not in itog:
                itog[name] = count
            else:
                itog[name] += count
        elif name == "Жемчуг+цветные":
            if name not in itog:
                itog[name] = count
            else:
                itog[name] += count

        itog["Замок"] += count
        itog["Протектор"] += 2 * count

        itog["Шарик"] += 2 * count
        itog["Штрих-код"] += count
        itog["Пакет"] += count



    def rasschet(self):
        self.main_menu.textBrowser.setText(f"    Кол-во нужных компонентов\n")
        for key, value in itog.items():
            self.main_menu.textBrowser.append(f"{key}-{value}")

    def Button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.lun(self.main_menu.comboBox.currentText()))
        self.main_menu.pushButton_3.clicked.connect(lambda: self.rasschet())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()