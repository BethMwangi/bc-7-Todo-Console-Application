from firebase import firebase
import collections
from models import Category, Items, Base

firebase = firebase.FirebaseApplication('https://todo-cli.firebaseio.com/', None)
result = firebase.post('/todo-cli' , user , )


class Firebase:
	def __init__(self):
		pass
	def up_category(self):
		category = []
		cat = session.query(Category).all()
		for x in cat:
			i = collections.OrderedDict()
			i['id'] = x[0]
			i['category'] = x[1]
			category.append(i)

		j = json.dumps(category)
        file = 'catObject.json'
        f = open(file,'w')
        print >> f, j


	def up_items(self):
		items = []
		item = session.query(Items).all()
		for x in item:
			i = collections.OrderedDict()
			i['id'] = x[0]
			i['category_id'] = x[1]
			i['items'] = x[2]
			category.append(i)

		j = json.dumps(category)
        file = 'itemObject.json'
        f = open(file,'w')
        print >> f, j


	 