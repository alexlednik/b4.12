"""
Напишите модуль users.py, который регистрирует новых пользователей. Скрипт должен запрашивать следующие данные:

имя
фамилию
пол
адрес электронной почты
дату рождения
рост
Все данные о пользователях сохраните в таблице user нашей базы данных sochi_athletes.sqlite3.
"""

import sqlalchemy as sa 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):

	__tablename__ = "user"

	id = sa.Column(sa.Integer, primary_key=True) 
	first_name = sa.Column(sa.Text)
	last_name = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	email = sa.Column(sa.Text)
	birthdate = sa.Column(sa.Text)
	height = sa.Column(sa.Float)


def connect_db():
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()


def get_user_data():
	print("Enter your details")
	first_name = input("Enter your name: ")
	last_name = input("Enter you last name: ")
	gender = input("Enter your gender (Male/Female): ")
	email = input("Your email: ")
	birthyear = input("Your year of birth: ")
	birthmonth = input("Your month of birth: ")
	birthday = input("Your day of birth: ")
	height = input("Your height: ")
	birthdate_tuple = (birthyear, birthmonth, birthday)
	birthdate = "-".join(birthdate_tuple)
	print(birthdate)

	user = User(
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height
	)
	return user

def main():

	session = connect_db()
	user = get_user_data()
	session.add(user)
	session.commit()

if __name__ == '__main__':
	main()
