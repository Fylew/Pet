from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import math
class App(QWidget):
    def __init__(self):
        self.start()
        self.Button()


    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()

    def lun(self):
        count = self.main_menu.spinBox.value()
        self.main_menu.textBrowser.setText(f"    Кол-во нужных компонентов\n\nПодвеска - {1 * count}шт\nЗамок - {1 * count}шт\nПротектор - {2 * count}шт"
                                           f"\nКольца - {2 * count}шт\nШарик - {2 * count}шт\nШтрих-код - {1 * count}шт\nПакет - {1 * count}шт\nБусины - {90 * count}шт"
                                           f"\nЦепочка - {13 * count}см\nТрос {42 * count}см\nУпаковок троса - {math.ceil((42 * count)/1500)}")

    def Button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.lun())
        self.main_menu.pushButton_2.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_3.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_4.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_5.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_6.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_7.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_8.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_9.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_10.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_11.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_12.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_13.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_14.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_15.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_16.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_17.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_18.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_19.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_20.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_21.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_22.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_23.clicked.connect(lambda:self.lun())
        self.main_menu.pushButton_24.clicked.connect(lambda:self.lun())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()