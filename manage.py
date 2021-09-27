from flask.cli import with_appcontext
from flask_migrate import Migrate
from app import app
import click

 

@click.command(name="yoyo")
@with_appcontext
def create():
    print("yooyo")

app.cli.add_command(create)
