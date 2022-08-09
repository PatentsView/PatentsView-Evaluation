import pandas as pd


def test_case_one():
    from pv_evaluation.metrics import cluster_precision_recall, pairwise_precision_recall

    reference = pd.Series([1, 1, 1, 2, 2, 3, 3, 4, 4])
    prediction = pd.Series([1, 1, 1, 2, 3, 2, 3, 4, 4])

    assert cluster_precision_recall(prediction, reference) == (0.5, 0.5)
    assert pairwise_precision_recall(prediction, reference) == (2 / 3, 2 / 3)
