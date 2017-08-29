###########################################################
# Based on https://stackoverflow.com/questions/34643620/how-can-i-split-my-click-commands-each-with-a-set-of-sub-commands-into-multipl

import click

@click.group()
@click.version_option()
def cli():
    pass #Entry Point

#############################################################
# First command group
#############################################################
@cli.group()
@click.pass_context
def wp(ctx):
    pass

@wp.group('zone')
def wp_zone():
    pass

@wp_zone.command('add')
@click.option('--jumpstart', '-j', default=True)
@click.option('--organization', '-o', default='')
@click.argument('url')
@click.pass_obj
#@__cf_error_handler
def wp_zone_add(ctx, url, jumpstart, organization):
    pass

@wp.group('record')
def wp_record():
    pass

@wp_record.command('add')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
#@__cf_error_handler
def wp_record_add(ctx, domain, name, type, content, ttl):
    pass

@wp_record.command('edit')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
#@__cf_error_handler
def wp_record_edit(ctx, domain):
    pass

###############################################################
# Next command group
###############################################################

@cli.group()
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
@click.argument('name', nargs=-1, required=True)
@click.pass_obj
def project_init(ctx, name):
    click.echo("Initialising a project")
    pass

#################################################################
# Give the tool a command line entry point for testing
#################################################################
if __name__ == '__main__':
    cli()