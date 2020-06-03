# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T5.2C.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

bl = LED(22)
gr = LED(27)
re = LED(17)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.blue = QtWidgets.QRadioButton(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(220, 300, 119, 27))
        self.blue.setAutoFillBackground(False)
        self.blue.setObjectName("blue")
        
        self.green = QtWidgets.QRadioButton(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(450, 300, 119, 27))
        self.green.setAutoFillBackground(True)
        self.green.setObjectName("green")
        
        self.red = QtWidgets.QRadioButton(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(710, 300, 119, 27))
        self.red.setAutoFillBackground(False)
        self.red.setObjectName("red")
        
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(470, 470, 99, 30))
        self.exit.setObjectName("exit")
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(470, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAutoFillBackground(False)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setIndent(0)
        self.title.setObjectName("title")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.blue.toggled.connect(lambda: self.ledSwitch(self.blue))
        self.green.toggled.connect(lambda: self.ledSwitch(self.green))
        self.red.toggled.connect(lambda: self.ledSwitch(self.red))
        
        self.exit.clicked.connect(self.end)
        
    def end(self):
        RPi.GPIO.cleanup()
        app.exit()
        
        
    def ledSwitch(self, b):
        if b.text() == "Blue LED":
            if b.isChecked() == True:
                bl.on()
            else:
                bl.off()
        if b.text() == "Green LED":
            if b.isChecked() == True:
                gr.on()
            else:
                gr.off()
        if b.text() == "Red LED":
            if b.isChecked() == True:
                re.on()
            else:
                re.off()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.blue.setText(_translate("MainWindow", "Blue LED"))
        self.green.setText(_translate("MainWindow", "Green LED"))
        self.red.setText(_translate("MainWindow", "Red LED"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.title.setText(_translate("MainWindow", "Task 5.2C GUI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
