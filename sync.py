from firebase import firebase
import click
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
	def upload_firebase(self):
		data={}
		category = []
		cat = session.query(Category).all()
		for x in cat:
			qry = session.query(Items).filter(Items.category_id==x.id)
			data[x.category]=[d.items for d in qry]

		name = click.prompt(click.style('Please enter your username:',  fg='cyan', bold=True))
		print Fore.GREEN  + 'Syncing..... '
		jsonData = firebase.put( '/todo-cli', name, data)
		if jsonData:
			print Fore.CYAN + 'Done!'
			exit()
		else:
			print 'Try again'

	def get_firebase(self):
		name = click.prompt(click.style('Please enter username?', fg = 'cyan' , bold=True))
		jsonData = firebase.get('/todo-cli' , name)
		for k in jsonData:
			#inserting category to database
			category = Category(category=k)
			session.add(category)
			session.commit()

			for i in jsonData[k]:
				s = select([Category])
				result = s.execute()
				for r in result:
					if r[1] == k:
						data = Items(category_id=r[0], items=i)
						session.add(data)
						session.commit()
						session.close()

		click.secho('Done', fg = 'yellow' , bold=True)				


