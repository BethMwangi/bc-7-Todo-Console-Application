import click

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
    click.echo(click.style('Hello World!', fg='blue', bold=True))

@click.command()
def create():
    cat = click.prompt(click.style('Create Category',  fg='green', bold=True))
    category = Category(category=cat)
    session.add(category)
    session.commit()
    click.echo(click.style('{} Successfully added to categories'.format(cat), fg='yellow', bold=True))

@click.command()
def add():
	'''
		querying database to display categories
		adding item to category
	'''
	s = select([Category])
	result = s.execute()
	if result:
		for row in result:
		    click.echo('[{}] {}'.format(str(row[0]),str(row[1])))

		select_cat = click.prompt(click.style('Select the number of category to add  add items' ,  fg='cyan', bold=True))





	else:
		click.echo('You have not created any category')
		create()

@click.command()
def view():
    click.echo(click.style('View Items',  fg='white', bold=True))

@click.command()
def delete():
    click.echo(click.style('Delete Item',  fg='red', bold=True))



#COMMANDS
cli.add_command(create)
cli.add_command(add)
cli.add_command(view)
cli.add_command(delete)


 




