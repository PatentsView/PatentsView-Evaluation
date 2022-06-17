from testbook import testbook


@testbook("tests/notebooks/templates/inventor-report.ipynb", execute=True)
def test_executable_notebook(tb):
    pass
