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
def create():
	create_todo()

@click.command()
def add():
	add_todo()

@click.command()
def view():
	view_todo()

@click.command()
def exit():
	exit_todo()





###MAIN PROGRAM RUNNING###
 
def start_todo():
	'''
		todo start  ====> Starts the app 
	'''

	click.echo(click.style("\n[1] Create new list of items.", fg ='white', bold = True))
	click.echo(click.style("[2] Add items to your category", fg ='white', bold = True))
	click.echo(click.style("[q] Quit.", fg ='white', bold = True))

	choice = str(click.prompt(click.style('Well what is your choice?',  fg = 'cyan', bold = True)))

	while choice != 'q':    
	    # Respond to the user's choice.
	    if choice == '1':
	    	create_todo()
	    elif choice == '2':
	        add_todo()
	    elif choice == 'q':
	        click.pause("Goodbye")
	        # exit_todo()
	    else:
	        click.echo("\nTry again\n")


###LOOPING FUNCTIONS ###
def todo_title():    
    # Display the title bar.
    print click.style("\t*** TASKIE: To do list application ***\n", fg ='cyan', bold = True, blink=True)
    print  click.style("\t*************************************\n", fg ='cyan', bold = True, blink=True)
   
   
def create_todo():
	'''
		todo create  ====> Create New Category 
	'''
	sleep(2)
	os.system('clear')

	todo_title()
	cat = click.prompt(click.style('Create Category',  fg = 'green', bold = True))


	category = Category(category=cat)
	session.add(category)
	session.commit()
	click.echo(click.style('{} Successfully added to categories'.format(cat), fg ='cyan', bold = True))
	add_todo()

def add_todo():
	'''
		todo add  ====> Add Items to category 
	'''
	sleep(2)
	os.system('clear')

	todo_title()

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

		view_todo()



	else:
		click.echo('You have not created any category')
		create()



def view_todo():
	'''
		todo View   ====> View Items 
	'''
	sleep(2)
	os.system('clear')

	todo_title()

	count = 1
	click.echo(click.style('TO DO LIST',  fg='green', bold=True , underline=True))
	s = select([Category])
	result = s.execute()
	if result:
		for row in result:
			q = session.query(Items).filter(Items.category_id==row[0]).all()

			click.echo(click.style( Fore.CYAN + str([count])+(Fore.GREEN + ' ' + row[1]),bold=True  ))
			count += 1


			for i in q:
				click.echo(click.style('>>>' + i.items  , fg='white', bold=True))
				
		start_todo()
	else:
		click.echo('Nothing to display')


### SYSTEM FUNCTION ###
def exit_todo():
	sys.exit()

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        sleep(0.25)



## FIREBASE ##
@click.command()
def save():
	'''
		todo save  ====> Sync item
	'''
	# up_items()
	# up_category()



#COMMANDS
cli.add_command(create)
cli.add_command(add)
cli.add_command(view)
cli.add_command(save)
cli.add_command(start)
cli.add_command(pager)





 





