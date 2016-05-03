import click
from prettytable import PrettyTable
import colorama 
from colorama import Fore, Back, Style
#DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from config import Category, Items, Base
 
engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()


####FUNCTIONS####
@click.group()
def cli():
    click.echo(click.style('Hello World!', fg = 'blue', bold = True))
  

@click.command()
def create():
	'''
		todo create  ====> Create New Category 
	'''
	cat = click.prompt(click.style('Create Category',  fg = 'green', bold = True))

	category = Category(category=cat)
	session.add(category)
	session.commit()
	click.echo(click.style('{} Successfully added to categories'.format(cat), fg ='yellow', bold = True))

@click.command()
def add():
	'''
		todo add  ====> Add Items to category 
	'''
	s = select([Category])
	result = s.execute()
	if result:
		for row in result:
		    click.echo('[{}] {}'.format(str(row[0]),str(row[1])))
		select_cat = click.prompt(click.style('Select the number of category to  add items' ,  fg='cyan', bold=True))
		# import ipdb
		# ipdb.set_trace()








		item = click.prompt(click.style('Create Item' ,  fg='cyan', bold=True))

		data = Items(category_id=select_cat, items=item)
		session.add(data)
		session.commit()



	else:
		click.echo('You have not created any category')
		create()

@click.command()
def view():
	'''
		todo View   ====> View Items 
	'''
	x = PrettyTable()
	click.echo(click.style('To do items',  fg='magenta', bold=True))
	s = select([Category])
	result = s.execute()
	if result:
		for row in result:
			q = session.query(Items).filter(Items.category_id==row[0]).all()
			click.echo(click.style('*****' + row[1] + '*****',underline=True ,  fg='cyan', bold=True , reverse=True))


			for i in q:
				click.echo(click.style('...' + i.items  , fg='white', bold=True))
	else:
		click.echo('Nothing to display')


@click.command()
def delete():
	'''
		todo delete  ====> Delete Item or category 
	'''
	click.echo(click.style('Delete Item',  fg='red', bold=True))



#COMMANDS
cli.add_command(create)
cli.add_command(add)
cli.add_command(view)
cli.add_command(delete)


###EXTRA STUFF###

 




