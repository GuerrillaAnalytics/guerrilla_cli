import click

from . import commands as group1


@click.group()
def cli():
    pass

cli.add_command(group1.version)
