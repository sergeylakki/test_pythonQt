import sqlalchemy

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://sergey:0000@127.0.0.1:3306/test_maria")