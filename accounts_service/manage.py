import click
from flask.cli import FlaskGroup

from accounts_service.app import create_app


def create_accounts_service(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_accounts_service)
def cli():
    """Main entry point"""

@cli.command("init")
def init():
    """Init application, create database tables
    """
    from accounts_service.extensions import db
    from accounts_service.models import Account
    click.echo("create database")
    db.drop_all()
    db.create_all()
    click.echo("done")


if __name__ == "__main__":
    cli()
