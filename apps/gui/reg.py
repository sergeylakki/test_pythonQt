# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self.window.show()

    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(432, 304)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 0, 341, 235))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InputName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InputName.setFont(font)
        self.InputName.setObjectName("InputName")
        self.verticalLayout.addWidget(self.InputName)
        self.InputPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InputPassword.setFont(font)
        self.InputPassword.setObjectName("InputPassword")
        self.verticalLayout.addWidget(self.InputPassword)
        self.InputPssword2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InputPssword2.setFont(font)
        self.InputPssword2.setObjectName("InputPssword2")
        self.verticalLayout.addWidget(self.InputPssword2)
        self.InputDate = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InputDate.setFont(font)
        self.InputDate.setCalendarPopup(True)
        self.InputDate.setTimeSpec(QtCore.Qt.LocalTime)
        self.InputDate.setObjectName("InputDate")
        self.verticalLayout.addWidget(self.InputDate)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BtnReg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BtnReg.setFont(font)
        self.BtnReg.setStyleSheet("background: green;\n"
"")
        self.BtnReg.setObjectName("BtnReg")
        self.horizontalLayout.addWidget(self.BtnReg)
        self.BtnCansel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BtnCansel.setFont(font)
        self.BtnCansel.setStyleSheet("background: red\n"
"")
        self.BtnCansel.setObjectName("BtnCansel")
        self.horizontalLayout.addWidget(self.BtnCansel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 22))
        self.menubar.setObjectName("menubar")
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Регистрация"))
        self.InputName.setPlaceholderText(_translate("RegisterWindow", "Имя пользователя"))
        self.InputPassword.setPlaceholderText(_translate("RegisterWindow", "Пароль"))
        self.InputPssword2.setPlaceholderText(_translate("RegisterWindow", "Повторить пароль"))
        self.InputDate.setSpecialValueText(_translate("RegisterWindow", "Дата рождения"))
        self.InputDate.setDisplayFormat(_translate("RegisterWindow", "dd.MM.yyyy"))
        self.BtnReg.setText(_translate("RegisterWindow", "ок"))
        self.BtnCansel.setText(_translate("RegisterWindow", "Отмена"))
