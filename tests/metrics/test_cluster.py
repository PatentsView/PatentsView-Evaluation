from testbook import testbook


@testbook("tests/notebooks/metrics/test_cluster.ipynb", execute=True)
def test_executable_notebook(tb):
    pass
