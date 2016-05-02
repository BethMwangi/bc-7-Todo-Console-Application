import click

#DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
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

@click.command()
def add():
    select_cat = click.prompt(click.style('Add item to category' ,  fg='cyan', bold=True))

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




