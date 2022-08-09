from testbook import testbook


@testbook("tests/notebooks/templates/inventor-report.ipynb", execute=True)
def test_inventor_report_notebook(tb):
    pass


@testbook("tests/notebooks/metrics/test_pairwise.ipynb", execute=True)
def test_pairwise_notebook(tb):
    pass


@testbook("tests/notebooks/metrics/test_cluster.ipynb", execute=True)
def test_cluster_notebook(tb):
    pass


@testbook("tests/notebooks/benchmark/benchmark-datasets.ipynb", execute=True)
def test_benchmark_datasets_notebook(tb):
    pass


@testbook("tests/notebooks/summary/inventor.ipynb", execute=True)
def test_summary_inventor_notebook(tb):
    pass


@testbook("tests/notebooks/estimators/test_estimators.ipynb", execute=True)
def test_estimators_notebook(tb):
    pass
