import re
import os

class ProjectException(Exception):
    pass

def check_project_name(project_name):
    """Check project name matches a pattern."""
    pattern = re.compile("^DS[0-9]{3}(_[a-zA-Z0-9]*)?")

    if not pattern.match(project_name) :
        raise ProjectException("Invalid format project name " + project_name)


def check_project_location(folder_location):
    """Check a folder does not exist and can be created"""
    if not os.path.exists(folder_location):
        raise OSError("Project folder location does not exist " + folder_location)