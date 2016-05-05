from firebase import firebase
import collections
from models import Category, Items, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
import ipdb

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
			print x
			qry = session.query(Items).filter(Items.category_id==x.id)
			data[x.category]=[d.items for d in qry]

		jsonData = firebase.post('/todo-cli',data)
		print jsonData

	# 		i = collections.OrderedDict()
	# 		i['id'] = x[0]
	# 		i['category'] = x[1]
	# 		category.append(i)

		# j = json.dumps(category)

	# 	print j
 #        file = 'catObject.json'
 #        f = open(file,'w')
 #        print >> f, j


	# def up_items(self):
	# 	items = []
	# 	item = session.query(Items).all()
	# 	for x in item:
	# 		i = collections.OrderedDict()
	# 		i['id'] = x[0]
	# 		i['category_id'] = x[1]
	# 		i['items'] = x[2]
	# 		category.append(i)

	# 	j = json.dumps(category)
 #        file = 'itemObject.json'
 #        f = open(file,'w')
 #        print >> f, j


	#  

if __name__ == '__main__':
	F = Firebase()
	F.up_category()