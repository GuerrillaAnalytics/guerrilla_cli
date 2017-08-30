###########################################################
# Based on https://stackoverflow.com/questions/34643620/how-can-i-split-my-click-commands-each-with-a-set-of-sub-commands-into-multipl
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from guerrilla.commands.project.project_cmd import project
from guerrilla.commands.wp.wp import wp

import click


@click.group()
@click.version_option()
def cli():
    pass #Entry Point

cli.add_command(project)
cli.add_command(wp)

#################################################################
# Give the tool a command line entry point for testing
#################################################################
if __name__ == '__main__':
    cli()