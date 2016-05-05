import os
import click
import sys
from prettytable import PrettyTable
import colorama 
from colorama import Fore, Back, Style
from time import sleep

#DATABASE
from sqlalchemy import exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from models import Category, Items, Base

# from sync import up_category, up_items 
engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()


####FUNCTIONS####
@click.group()
def cli():
	"""To Do Apllication

	This commandline app allows you to create and store todo items to keep track of your productivity
	"""
	os.system('clear')


@click.command()  
def title():
	todo_title()

@click.command()  
def start():
	todo_title()
	start_todo()

@click.command()
@click.argument('name', metavar='<name>')
def create(name):
	create_todo(name)

@click.command()
@click.argument('name', metavar='<name>')
def open(name):
	open_todo(name)

@click.command()
@click.argument('name' , metavar='<name>')
@click.argument( 'item' , metavar='<item>')
def add(name , item):
	add_todo(name ,item)


@click.command()
@click.argument('name' , metavar='<name>')
def list(name):
	list_todo(name)

@click.command()
def list_todos():
	list_todos_all()

@click.command()
def exit():
	exit_todo()





###MAIN PROGRAM RUNNING###
 
def start_todo():
	'''
		todo start  ====> Starts the application 
	'''

	# click.echo(click.style("\n[1] Create new list of todo.", fg ='white', bold = True))
	# click.echo(click.style("[2] Add items to your category", fg ='white', bold = True))
	# click.echo(click.style("[q] Quit.", fg ='white', bold = True))

	choice = str(click.prompt(click.style('>>>',  fg = 'cyan', bold = True)))

	while choice != 'q':    
	    # Respond to the user's choice.
	    if 'create todo' in choice:
	    	print 'creating'
	    elif 'open todo' in choice:
	        print 'openning'
	    elif 'list todo' in choice:
	        print 'listing'
	    elif choice:
	        exit_todo()
	    else:
	        click.echo("\nTry again\n")



###LOOPING FUNCTIONS ###
def todo_title():    
    # Display the title bar.
    print click.style("\t*** TASKIE: To do list application ***\n", fg ='cyan', bold = True, blink=True)
    print  click.style("\t*************************************\n", fg ='cyan', bold = True, blink=True)
   
   
def create_todo(name):
	'''
		todo create <list name>  ====> Creates New List
	'''
	
	os.system('clear')

	todo_title()
	cat = name


	category = Category(category=cat)
	session.add(category)
	session.commit()
	click.secho('{} Successfully added to categories add items'.format(cat), fg ='cyan', bold = True)

	open_todo(name)

   
def open_todo(name):
	'''
		todo open <list name> ====> Open List 
	'''
	
	os.system('clear')

	todo_title()

	s = select([Category])
	result = s.execute()
	for r in result:
		if r[1] == name:
			q = session.query(Items).filter(Items.category_id==r[0]).all()
			click.secho(name.upper(), fg='cyan', bold=True, underline=True)
			for i in q:
				click.secho('>>>' + i.items, fg='white', bold=True )

	item = click.prompt(click.style('>>',  fg='green', bold=True))
	if item == 'q':
		exit()
	elif item == 'done':
		list_todo(name)	
	else:			
		add_todo(name, item)			

def add_todo(name, item):
	'''
		todo add <list-name> <item>  ====> Add Items to List 
	'''
	
	os.system('clear')

	todo_title()

	s = select([Category])
	result = s.execute()
	for r in result:
		if r[1] == name:
			data = Items(category_id=r[0], items=item)
			session.add(data)
			session.commit()
			open_todo(name)



def list_todo(name):
	'''
		todo list <list-name>   ====> View List items 
	'''
	
	os.system('clear')

	todo_title()

	s = select([Category])
	result = s.execute()
	for r in result:
		if r[1] == name:
			q = session.query(Items).filter(Items.category_id==r[0]).all()
			click.secho(name  , fg='cyan', bold=True)
			for i in q:
				click.secho('>>>' + i.items  , fg='white', bold=True)

			if click.confirm('Do you want to continue?'):
				click.secho('Well done!' , fg='green', bold=True)



def list_todos_all():
	'''
		todo list_todo   ====> View All List
	'''
	os.system('clear')

	todo_title()

	count = 1
	click.echo(click.style('TO DO LIST',  fg='green', bold=True , underline=True))
	s = select([Category])
	result = s.execute()
	if result:
		for row in result:
			q = session.query(Items).filter(Items.category_id==row[0]).all()

			click.echo(click.style( Fore.CYAN + str([count])+(Fore.CYAN + ' ' + row[1]),bold=True  ))
			count += 1


			for i in q:
				click.echo(click.style('>>>' + i.items  , fg='white', bold=True))
				
		start_todo()
	else:
		click.echo('Nothing to display')





### SYSTEM FUNCTION ###
def exit_todo():
	pass

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        sleep(1)



## FIREBASE ##
@click.command()
def save():
	'''
		todo save  ====> Sync item
	'''
	# up_items()
	# up_category()



#COMMANDS
cli.add_command(start)
cli.add_command(create)
cli.add_command(open)
cli.add_command(add)
cli.add_command(list)
cli.add_command(list_todos)
cli.add_command(save)






 





