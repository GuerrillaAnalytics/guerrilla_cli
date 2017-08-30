import click
from guerrilla.commands.project.utils import *
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
@click.argument('name', nargs=1, required=True)
@click.argument('location', required=True)

@click.pass_obj
def project_init(ctx, name,location):
    click.echo(click.style("Initialising a project", fg='green'))
    click.echo(click.style("Name "+ name , fg='green'))
    click.echo(click.style("Location: " + location, fg='green'))

    # Check the project name is correct
    try:
        check_project_name(name)
    except ProjectException as e:
        click.echo(click.style(e.args[0], fg='red'))

    # Check the project location exists
    try:
        check_project_location(location)
    except OSError as e:
        click.echo(click.style(e.args[0], fg='red'))

    project_path=os.path.join(location,name)

    if not os.path.exists(project_path):
        os.makedirs(project_path)
    pass
