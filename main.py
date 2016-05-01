import click

@click.command()
def cli():
	click.echo(click.style('Hello World!', fg='green'))


	