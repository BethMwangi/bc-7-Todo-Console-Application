import click

@click.command()
def hello():
	click.echo(click.style('Hello World!', fg='green'))
if __name__=='__main__':
	hello()


	