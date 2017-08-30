import click
import re
import os
from pathlib import Path
import configparser

class ProjectException(Exception):
    pass

def check_project_name(project_name):
    """Check project name matches a pattern."""
    pattern = re.compile("^DS[0-9]{3}(_([a-zA-Z0-9])*)?")

    if re.match(pattern,project_name) is None:
        raise ProjectException("Invalid format project name: " + project_name)


def check_project_location(folder_location):
    """Check a folder does not exist and can be created"""
    if not os.path.exists(folder_location):
        raise OSError("Project folder location does not exist " + folder_location)


def initialise_project(name,location):

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

    # if the folder does not exist, create it
    if not os.path.exists(project_path):
        os.makedirs(project_path)

    # Check if a config file exists in the folder already
    config = configparser.ConfigParser()
    cfg=Path(os.path.join(location,"guerrilla.cfg"))
    if cfg.is_file():
        click.confirm('A config file already exists in the folder. Do you want to continue?', abort=True)
        config.read(cfg)
        # TODO config activities

    # Make the pm folder tree
    pm_folder = os.path.join(project_path, "pm")
    if not os.path.exists(pm_folder):
        click.echo("creating pm folder")
        os.makedirs(pm_folder)

    initiate_folder=os.path.join(pm_folder,"01_initiate")
    if not os.path.exists(initiate_folder):
        click.echo("creating initiate folder")
        os.makedirs(initiate_folder)

    plan_folder=os.path.join(pm_folder,"02_plan")
    if not os.path.exists(plan_folder):
        click.echo("creating plan folder")
        os.makedirs(plan_folder)

    execute_folder=os.path.join(pm_folder,"03_execute")
    if not os.path.exists(execute_folder):
        click.echo("creating execute folder")
        os.makedirs(execute_folder)

    control_folder=os.path.join(pm_folder,"04_control")
    if not os.path.exists(control_folder):
        click.echo("creating control folder")
        os.makedirs(control_folder)

    close_folder=os.path.join(pm_folder,"05_close")
    if not os.path.exists(close_folder):
        click.echo("creating closefolder")
        os.makedirs(close_folder)

    # Make the wp folder
    wp_folder = os.path.join(project_path, "wp")
    if not os.path.exists(wp_folder):
        click.echo("creating wp folder")
        os.makedirs(wp_folder)

    pass
