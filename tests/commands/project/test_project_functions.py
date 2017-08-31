import pytest
import tempfile
import os
from click.testing import CliRunner
from guerrilla.commands.project import project_functions
from guerrilla.commands.project.project_functions import ProjectException

@pytest.fixture
def runner():
    return CliRunner()


def test_check_project_name_wrong_case(runner):
    with pytest.raises(ProjectException) as exc_info:
        project_functions.check_project_name(project_name="ds001")

def test_check_project_name_start(runner):
    with pytest.raises(ProjectException) as exc_info:
        project_functions.check_project_name(project_name="wrongStart001")

def test_initialise_project(runner):
    p = tempfile.mkdtemp()
    project_functions.initialise_project("DS001",p)
    assert os.path.exists(os.path.join(p,"DS001")) == 1
    assert os.path.exists(os.path.join(p,"DS001","wp")) == 1
    assert os.path.exists(os.path.join(p,"DS001","pm")) == 1
# def test_cli_with_option(runner):
#     result = runner.invoke(cli.cli, ['--as-cowboy'])
#     assert not result.exception
#     assert result.exit_code == 0
#     assert result.output.strip() == 'Howdy, world.'
#
#
# def test_cli_with_arg(runner):
#     result = runner.invoke(cli.cli, ['Enda'])
#     assert result.exit_code == 0
#     assert not result.exception
#     assert result.output.strip() == 'Hello, Enda.'
