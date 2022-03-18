import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from werkzeug.security import check_password_hash, generate_password_hash
from apps.gui.reg import Ui_RegisterWindow
from apps.gui.auth import Ui_AuthWindow
from apps.gui.contact import Ui_Contacts
from datetime import date
from apps import engine
from model import Base, User, Contact
from sqlalchemy.orm import sessionmaker
from PyQt5 import QtGui


class DBInterface:
    def __init__(self):
        connection = engine.connect()
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        self.user_id = None

    def register_user(self, name, password, password2, date):
        session = self.Session()
        new_user = User(name=name, password=generate_password_hash(password), date_birth=date)
        session.add(new_user)
        session.commit()
        self.user_id = new_user.id
        print("registr")

    def get_contacts(self, start_chars):
        session = self.Session()
        contacts_list = []
        for i in start_chars:
            print(i)
            contacts = session.query(Contact).filter(Contact.name.ilike(f"{i}%"))
            print(contacts.count())
            for contact in contacts:
                contacts_list.append([contact.name, contact.phone, contact.date_birth])
        contacts_list.append(["", "", ""])
        return contacts_list

    def create_contact(self,name,phone,date_birth):
        if self.user_id != None:
            session = self.Session()
            date_birth = datetime.datetime.strptime(date_birth, "%Y-%m-%d")
            print(type(date_birth))
            contacts = session.query(Contact).filter(Contact.name == name, Contact.phone == phone, Contact.date_birth == date_birth)
            for contact in contacts:
                if contact.user_id == self.user_id:
                    print("user_allready")
                    return False
            new_user = Contact(name=name, phone=phone, date_birth=date_birth, user_id=self.user_id)
            session.add(new_user)
            try:
                session.commit()
                print("registr:", name, phone, date_birth)
            except Exception as error:
                print("error", error)

    def get_user_name(self):
        session = self.Session()
        user = session.query(User).get(self.user_id)
        return user.name

    def auth_user(self, name, password):
        session = self.Session()
        users = session.query(User).filter(User.name == name)
        print(users[0].name)
        if len(list(users)) == 1:
            if check_password_hash(users[0].password, password):
                self.user_id = users[0].id
                return True
            else:
                print("password error")
        print("user not found")
        return False



class ContactWindow(QMainWindow):
    def __init__(self, db):
        super(ContactWindow, self).__init__()
        self.window = Ui_Contacts()
        self.window.setupUi(self)
        self.db = db
        self.new_table = []
        self.window.labelName.setText(db.get_user_name())
        for i in range(len(self.window.tables)):
            self.create_tables(i)

        self.window.BtnSave.clicked.connect(self.save_change)

    def save_change(self):
        for table in self.new_table:
            for i in range(table.rowCount()):
                if table.index(i, 0).data() and table.index(i, 1).data() and table.index(i, 1).data():
                    print(table.index(i, 0).data(), table.index(i, 1).data(), table.index(i, 2).data())
                    self.db.create_contact(table.index(i, 0).data(), table.index(i, 1).data(), table.index(i, 2).data())




    def create_tables(self, n):
        headers = ["Имя", "Телефон", "Дата рождения"]
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(headers)
        items = self.db.get_contacts(self.window.btn_name[n])
        model.rowCount()
        for row_number, row_data in enumerate(items):
            tableitem = []
            model.insertRow(row_number)
            for i, value in enumerate(row_data):
                item = QtGui.QStandardItem(str(value))
                item.setSelectable(True)
                tableitem.append(item)
            model.insertRow(row_number, tableitem)
        self.window.tables[n].setModel(model)
        for i in range(3):
            self.window.tables[n].setColumnWidth(i, 300)
        self.new_table.append(model)


class RegisterUserWindow(QMainWindow):
    def __init__(self, db):
        super(RegisterUserWindow, self).__init__()
        self.window = Ui_RegisterWindow()
        self.window.setupUi(self)
        self.window.BtnReg.clicked.connect(self.registr_user)
        self.db = db

    def registr_user(self):
        name = self.window.InputName.text()
        password = self.window.InputPassword.text()
        password2 = self.window.InputPssword2.text()
        date_birth = self.window.InputDate.date().toPyDate()
        print(name, password, password2, date_birth, date.today())
        self.db.register_user(name, password, password2, date_birth)
        self.close()
        self.contact_window = ContactWindow(self.db)
        self.contact_window.show()
        #self.setWindowTitle('Window2')


class AuthUserWindow(QMainWindow):
    def __init__(self, db):
        super(AuthUserWindow, self).__init__()
        self.window = Ui_AuthWindow()
        self.window.setupUi(self)
        self.window.BtnReg.clicked.connect(self.open_reg)
        self.window.BtnIn.clicked.connect(self.auth_user)
        self.window.BtnCansel.clicked.connect(self.close)
        self.db = db

    def open_reg(self):
        #self.close()
        self.register_user = RegisterUserWindow(self.db)
        self.register_user.show()

    def auth_user(self):
        name = self.window.InputName.text()
        password = self.window.InputPassword.text()
        if self.db.auth_user(name,password):
            self.contact = ContactWindow(self.db)
            self.contact.show()
        else:
            print("error")

    def close(self):
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DBInterface()
    w = AuthUserWindow(db)
    w.show()
    sys.exit(app.exec_())