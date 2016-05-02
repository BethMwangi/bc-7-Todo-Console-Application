import click


####FUNCTIONS####
@click.group()
def cli():
    click.echo(click.style('Hello World!', fg='blue', bold=True))

@click.command()
def create():
    click.echo(click.style('Create Category',  fg='green', bold=True))

@click.command()
def add():
    click.echo(click.style('Add item to category' ,  fg='cyan', bold=True))

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


