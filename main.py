import click

__version__ = "0.1.0"

@click.command("version")
def version():
    click.echo(__version__)

@click.command("hello")
def hello():
    click.echo("Hello, World!")

if __name__ == "__main__":
    hello()
