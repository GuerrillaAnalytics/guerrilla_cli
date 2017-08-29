import click
from guerrilla.commands.project.utils import *

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

@click.pass_obj
def project_init(ctx, name):
    click.echo(click.style("Initialising a project", fg='green'))
    try:
        check_project_name(name)
    except ProjectException as e:
        click.echo(click.style(e.args[0], fg='red'))


    pass
