from firebase import firebase
import collections
from models import Category, Items, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from colorama import Fore, Back, Style

firebase = firebase.FirebaseApplication('https://todo-cli.firebaseio.com/', None)
# jsonData = firebase.post('/todo-cli'  )

# from sync import up_category, up_items 
engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Firebase:
	def up_category(self):
		data={}
		category = []
		cat = session.query(Category).all()
		for x in cat:
			qry = session.query(Items).filter(Items.category_id==x.id)
			data[x.category]=[d.items for d in qry]

		name = raw_input('Please enter your username:' ,  fg='green', bold=True , underline=True)
		print Fore.GREEN  + 'Syncing..... '
		jsonData = firebase.put('/todo-cli', name, data)
		if jsonData:
			print Fore.CYAN + 'Done!'

	def get(self):
			r = firebase.get('/todo-cli', name, data)	
			print r	




if __name__ == '__main__':
	F = Firebase()
	F.get()