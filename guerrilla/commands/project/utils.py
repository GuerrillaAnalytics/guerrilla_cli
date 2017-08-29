import re


class ProjectException(Exception):
    pass

def check_project_name(project_name):
    pattern = re.compile("^DS[0-9]{3}(_[a-zA-Z0-9]*)")

    if not pattern.match(project_name) :
        raise ProjectException("Invalid format project name")