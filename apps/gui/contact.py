# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contact.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Contacts(object):
    def setupUi(self, Contacts):
        Contacts.setObjectName("Contacts")
        Contacts.resize(930, 900)
        font = QtGui.QFont()
        font.setPointSize(14)
        Contacts.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Contacts)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 917, 900))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(500, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("color: blue;\n"
"")
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.horizontalLayout.addWidget(self.labelName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.BtnSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BtnSave.setObjectName("BtnSave")
        self.verticalLayout.addWidget(self.BtnSave)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.vboxlayout.setObjectName("vboxlayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.btn_name = ["АБ", "ВГ", "ДЕ", "ЖЗИЙ", "КЛ", "МН", "ОП", "РС", "ТУ", "ФХ", "ЦЧШЩ", "ЬЫЪЭ", "ЮЯ"]
        self.menu_btn = []
        self.tables = []
        for i, k in enumerate(self.btn_name):
            self.menu_btn.append(QtWidgets.QWidget())
            self.menu_btn[i].setObjectName(k)

            self.tables.append(QtWidgets.QTableView(self.menu_btn[i]))
            self.tables[i].setGeometry(QtCore.QRect(0, 0, 881, 800))
            self.tables[i].columnWidth(500)
            self.tables[i].setObjectName("tableView_2")
            self.tabWidget.addTab(self.menu_btn[i], "")
        self.vboxlayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.vboxlayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        Contacts.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Contacts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 27))
        self.menubar.setObjectName("menubar")
        Contacts.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Contacts)
        self.statusbar.setObjectName("statusbar")
        Contacts.setStatusBar(self.statusbar)

        self.retranslateUi(Contacts)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Contacts)

    def retranslateUi(self, Contacts):
        _translate = QtCore.QCoreApplication.translate
        Contacts.setWindowTitle(_translate("Contacts", "Контакты"))
        self.label_2.setText(_translate("Contacts", "Вы зашли как: "))
        self.BtnSave.setText(_translate("Contacts", "Сохранить изменения"))
        for i, btn in enumerate(self.menu_btn):
            self.tabWidget.setTabText(self.tabWidget.indexOf(btn), _translate("Contacts",self.btn_name[i]))
