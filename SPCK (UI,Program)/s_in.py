
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 550, 650))
        self.frame.setStyleSheet("background:#9b9b9b\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(49, 30, 450, 570))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background:#ffffff;\n"
"border-radius:20px;\n"
"border: 2px solid white\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 20, 170, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 0px solid\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(15)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 0px solid\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 381, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:2px solid grey;\n"
"padding-left:15px")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 0px solid\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 0px solid\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 300, 381, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:2px solid grey;\n"
"padding-left:15px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(280, 360, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 0px solid\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(90, 500, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 0px solid\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(280, 500, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 0px solid\n"
"")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(69, 419, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:2px solid grey; \n"
"background:#00aeff;\n"
"color:#ffffff")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(40, 360, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
        self.lineEdit_2.raise_()
        self.checkBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sign in"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "to get started"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Forgot password?"))
        self.label_6.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.label_7.setText(_translate("MainWindow", "Sign up"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
        self.checkBox.setText(_translate("MainWindow", "Show password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
