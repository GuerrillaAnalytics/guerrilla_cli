import click
from guerrilla.commands.project.project_functions import *
import os

@click.group()
@click.pass_context
def project(ctx):
    pass


@project.command('add')
@click.option('--alert', '-a', default=True)
@click.argument('name')
@click.argument('url')
@click.pass_obj
def project_add(ctx, name, url, alert):
    pass


@project.command('init')
@click.argument('name', nargs=1,required=True)
@click.argument('location',nargs=1, required=True)
@click.pass_obj
def project_init(ctx, name,location):
    click.echo(click.style("Initialising a project", fg='green'))
    click.echo(click.style("Name "+ name , fg='green'))
    click.echo(click.style("Location: " + location, fg='green'))

    initialise_project(name,location)