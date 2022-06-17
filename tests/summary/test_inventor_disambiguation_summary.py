from testbook import testbook


@testbook("tests/notebooks/summary/inventor.ipynb", execute=True)
def test_executable_notebook(tb):
    pass
