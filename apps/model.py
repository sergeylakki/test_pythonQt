from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from apps import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(40), nullable=False, unique=True)
    password = Column('password', String(200), nullable=False)
    date_birth = Column('date_birth', DateTime, nullable=False)

    def __init__(self, name, password, date_birth):
        self.name = name
        self.password = password
        self.date_birth = date_birth

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.password, self.date_birth)


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(40), nullable=False)
    phone = Column('phone', String(12), nullable=False)
    date_birth = Column('date_birth', Date(), nullable=False)
    user_id = Column('user_id', ForeignKey('users.id'), nullable=False)

    def __init__(self, name,  phone, date_birth, user_id):
        self.name = name
        self.date_birth = date_birth
        self.phone = phone
        self.user_id = user_id

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.phone, self.date_birth)


# Создание таблицы
Base.metadata.create_all(engine)