from testbook import testbook


@testbook("tests/notebooks/templates/inventor-report.ipynb", execute=True)
def test_executable_notebook(tb):
    pass

@testbook("tests/notebooks/metrics/test_pairwise.ipynb", execute=True)
def test_executable_notebook(tb):
    pass

@testbook("tests/notebooks/metrics/test_cluster.ipynb", execute=True)
def test_executable_notebook(tb):
    pass

@testbook("tests/notebooks/benchmark/benchmark-datasets.ipynb", execute=True)
def test_executable_notebook(tb):
    pass

@testbook("tests/notebooks/summary/inventor.ipynb", execute=True)
def test_executable_notebook(tb):
    pass
