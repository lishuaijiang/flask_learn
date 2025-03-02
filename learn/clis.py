import click
from datetime import datetime


@click.command("greet")
@click.argument("name")
def greet(name):
    """
    Greet a user by name.
    """
    click.echo(f"Hello, {name}! Welcome to Flask with Click!")


@click.command("current-time")
def current_time():
    """
    Display the current time in the format YYYY-MM-DD HH:MM:SS.
    """
    now = datetime.now()
    click.echo(f"Current time is {now.strftime('%Y-%m-%d %H:%M:%S')}")
