# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auth.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthWindow():

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self.window.show()

    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.setEnabled(True)
        AuthWindow.resize(533, 361)
        AuthWindow.setProperty("color_btn_in", "")
        self.centralwidget = QtWidgets.QWidget(AuthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InputName = QtWidgets.QLineEdit(self.centralwidget)
        self.InputName.setGeometry(QtCore.QRect(60, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.InputName.setFont(font)
        self.InputName.setInputMask("")
        self.InputName.setText("")
        self.InputName.setMaxLength(32767)
        self.InputName.setObjectName("InputName")
        self.InputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.InputPassword.setGeometry(QtCore.QRect(60, 70, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.InputPassword.setFont(font)
        self.InputPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.InputPassword.setInputMask("")
        self.InputPassword.setText("")
        self.InputPassword.setMaxLength(32767)
        self.InputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InputPassword.setObjectName("InputPassword")
        self.BtnIn = QtWidgets.QPushButton(self.centralwidget)
        self.BtnIn.setGeometry(QtCore.QRect(30, 120, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 255, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.BtnIn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BtnIn.setFont(font)
        self.BtnIn.setAutoFillBackground(False)
        self.BtnIn.setStyleSheet("background: rgb(43, 255, 36);\n"
"border-radius: 10px;\n"
"")
        self.BtnIn.setObjectName("BtnIn")
        self.BtnReg = QtWidgets.QPushButton(self.centralwidget)
        self.BtnReg.setGeometry(QtCore.QRect(180, 120, 181, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.BtnReg.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BtnReg.setFont(font)
        self.BtnReg.setAutoFillBackground(False)
        self.BtnReg.setStyleSheet("background: rgb(189, 189, 189);\n"
"border-radius: 10px;\n"
"")
        self.BtnReg.setObjectName("BtnReg")
        self.BtnCansel = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCansel.setGeometry(QtCore.QRect(370, 120, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 27, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.BtnCansel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BtnCansel.setFont(font)
        self.BtnCansel.setAutoFillBackground(False)
        self.BtnCansel.setStyleSheet("background: rgb(252, 27, 32);\n"
"border-radius: 10px;\n"
"")
        self.BtnCansel.setObjectName("BtnCansel")
        self.CbRememberPassword = QtWidgets.QCheckBox(self.centralwidget)
        self.CbRememberPassword.setGeometry(QtCore.QRect(110, 180, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CbRememberPassword.setFont(font)
        self.CbRememberPassword.setObjectName("CbRememberPassword")
        self.CbViewPassword = QtWidgets.QCheckBox(self.centralwidget)
        self.CbViewPassword.setGeometry(QtCore.QRect(110, 210, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CbViewPassword.setFont(font)
        self.CbViewPassword.setObjectName("CbViewPassword")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 211, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(9, 0, 255);\n"
"background: rgba(255, 255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        AuthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AuthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 22))
        self.menubar.setObjectName("menubar")
        AuthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AuthWindow)
        self.statusbar.setObjectName("statusbar")
        AuthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Вход"))
        self.InputName.setPlaceholderText(_translate("AuthWindow", "Имя пользователя"))
        self.InputPassword.setPlaceholderText(_translate("AuthWindow", "Пароль"))
        self.BtnIn.setText(_translate("AuthWindow", "Вход"))
        self.BtnIn.setProperty("color", _translate("AuthWindow", "background: rgb(255,0,0);"))
        self.BtnReg.setText(_translate("AuthWindow", "Регистрация"))
        self.BtnCansel.setText(_translate("AuthWindow", "Отмена"))
        self.CbRememberPassword.setText(_translate("AuthWindow", "Запомнить меня"))
        self.CbViewPassword.setText(_translate("AuthWindow", "Показать пароль"))
        self.pushButton.setText(_translate("AuthWindow", "Забыли пароль?"))
