import sqlalchemy
from settings import db_password, db_port, db_name, db_user, db_host

engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")