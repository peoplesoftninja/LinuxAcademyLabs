
import pytest

from hr import cli
@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_fails_without_arguments_passed(parser):
    """
    Error is raised if no arguments are passed
    """

    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_suceeds_with_path(parser):
    """
    With a path parser succeeds"
    """
    args = parser.parse_args(['/some/path'])
    assert args.path == '/some/path'
    assert args.export == False

def test_parser_export_value_true(parser):
    """
    export value is true if given
    """
    args = parser.parse_args(['--export','/some/path'])
    assert args.export == True
