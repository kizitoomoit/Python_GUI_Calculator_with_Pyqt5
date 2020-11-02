from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import sqrt

import sys
from PyQt5.uic import loadUiType

ui,_ = loadUiType('calculator1.ui')

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        #self.initUI()
        self.setWindowTitle('Calculator')

    def initUI(self):
        pass
        #self.lineEdit.setValidator(QIntValidator)

    def clear_Screen(self):
        self.lineEdit.clear()

    def bckspace(self):
        self.lineEdit.backspace()



    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.clear_Screen)
        self.pushButton_4.clicked.connect(self.bckspace)
        self.pushButton_13.clicked.connect(self.one)
        self.pushButton_14.clicked.connect(self.two)
        self.pushButton_15.clicked.connect(self.three)
        self.pushButton_9.clicked.connect(self.four)
        self.pushButton_10.clicked.connect(self.five)
        self.pushButton_11.clicked.connect(self.six)
        self.pushButton_5.clicked.connect(self.seven)
        self.pushButton_6.clicked.connect(self.eight)
        self.pushButton_7.clicked.connect(self.nine)
        self.pushButton_19.clicked.connect(self.Dot)
        self.pushButton_18.clicked.connect(self.zero)
        self.pushButton_20.clicked.connect(self.Equal)
        self.pushButton_3.clicked.connect(self.Mult)
        self.pushButton_2.clicked.connect(self.Divi)
        self.pushButton_8.clicked.connect(self.Minus)
        self.pushButton_12.clicked.connect(self.Ad)
        self.pushButton_17.clicked.connect(self.Percnt)



    def one(self):
        global newNum
        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)
        self.lineEdit.setText(self.lineEdit.text() + setNum)


    def two(self):

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)


    def three(self):
        global newNum

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)

    def four(self):
        global neNum
        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)


    def five(self):
        global newNum

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)


    def six(self):
        global newNum

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)


    def seven(self):
        global newNum

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)


    def eight(self):
        global newNum

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)


    def nine(self):
        global newNum

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)

    def zero(self):
        global newNum

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        self.lineEdit.setText(self.lineEdit.text() + setNum)

    def Dot(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + ".")


    def Mult(self):
        #appending lineedit text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "*")
    def Minus(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "-")

    def Percnt(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "%")
    def Divi(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "/")

    def Ad(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "+")

    def Equal(self):
        equation = self.lineEdit.text()

        try:
            #getting answer
            ans = eval(equation)

            #setting text to lineEdit
            self.lineEdit.setText(str(ans))

        except:
            #setting text to lineEdit
            self.lineEdit.setText("WRONG INPUT!")


    def Num(self):
        global num
        global  newNum
        global  opVar

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        if opVar == False:
            self.line.setText(self.line.text() + setNum)
        else:
            self.line.setText(setNum)
            opVar = False



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    #window.setWindowTitle("Calculator")
    app.exec_()

if __name__ == '__main__':
    main()
