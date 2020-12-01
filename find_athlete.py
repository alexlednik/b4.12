""" 
Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:

запросить идентификатор пользователя;
если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
если пользователя с таким идентификатором нет, вывести соответствующее сообщение
"""

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from users import User
import datetime
import time 


DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Athelete(Base):

	__tablename__ = "athelete"

	id = sa.Column(sa.Integer, primary_key = True)
	age = sa.Column(sa.Integer)
	birthdate = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	height = sa.Column(sa.Float)
	name = sa.Column(sa.Text)
	weight = sa.Column(sa.Integer)
	gold_medals = sa.Column(sa.Integer)
	silver_medals = sa.Column(sa.Integer)
	bronze_medals = sa.Column(sa.Integer)
	total_medals = sa.Column(sa.Integer)
	sport = sa.Column(sa.Text)
	country = sa.Column(sa.Text)


def get_closest_indices(user_value, atheletes_values):
	diffs = [abs(user_value-athelete_value) if athelete_value is not None else 1000 for athelete_value in atheletes_values]

	closest = min(diffs)
	indices = [i+1 for i, x in enumerate(diffs) if x == closest]

	return indices


def closest_bd(query_user, query_atheletes): 
 	
	user_birthdate_list = [user.birthdate for user in query_user]
	user_birthdate = strtotimestamp(user_birthdate_list[0])

	atheletes_birthdates = list(map(strtotimestamp, [athelete.birthdate for athelete in query_atheletes]))

	return get_closest_indices(user_birthdate, atheletes_birthdates)


def closest_height(query_user, query_atheletes):

	user_height_list = [user.height for user in query_user]

	atheletes_heights = [athelete.height for athelete in query_atheletes]

	return get_closest_indices(user_height_list[0], atheletes_heights)


def connect_db():
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)

	return session()


def strtotimestamp(s):
	d = s.split()[0]
	date = d.split('-')

	return datetime.datetime(int(date[0]), int(date[1]), int(date[2]))


def find_match(id, session):
	query_user = session.query(User).filter(User.id == id).all()
	if query_user:
		query_atheletes = session.query(Athelete).all()

		bd_indices = closest_bd(query_user, query_atheletes)
		height_indices = closest_height(query_user, query_atheletes)

		print("Closest Birthdates have: ")
		print(bd_indices)
		for i in bd_indices:
			print(query_atheletes[i].birthdate)
		print("---------")
		print("Closest height have: ")
		print(height_indices)
		for i in height_indices:
			print(query_atheletes[i].height)
	else: 
		print("No such user")


def main():
	id = input("Enter user id: ")
	session = connect_db()
	find_match(id, session)


if __name__ == '__main__':
	main()