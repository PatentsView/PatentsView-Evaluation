import pytest
import pandas as pd

@pytest.fixture
def reference():
    return pd.Series([0, 0, 1, 1, 1, 2, 3, 4, 4, 5, 6 ,7, 8, 8, 8, 8, 9, 0, 11, 11])

@pytest.fixture
def sampling_types():
    return ["record", "cluster", "cluster_block", "single_block"]

def test_edge_cases(reference):
    from pv_evaluation.estimators import pairwise_precision_estimator, pairwise_recall_estimator

    # Precision
    # Bias adjustment makes the following be at around 1.05 instead of 1.0.
    #assert pairwise_precision_estimator(reference, reference, sampling_type="cluster", weights="uniform") == 1.0
    assert pairwise_precision_estimator(reference, reference, sampling_type="cluster_block", weights="uniform") == 1.0
    assert pairwise_precision_estimator(reference, reference, sampling_type="single_block", weights="uniform") == 1.0
    assert pairwise_precision_estimator(reference, reference, sampling_type="single_block", weights="cluster_size") == 1.0

    # Recall
    assert pairwise_recall_estimator(reference, reference, sampling_type="record", weights="uniform") == 1.0
    assert pairwise_recall_estimator(reference, reference, sampling_type="cluster", weights="uniform") == 1.0
    assert pairwise_recall_estimator(reference, reference, sampling_type="cluster_block", weights="uniform") == 1.0
    assert pairwise_recall_estimator(reference, reference, sampling_type="single_block", weights="uniform") == 1.0
    
    assert pairwise_recall_estimator(reference, reference, sampling_type="cluster", weights="cluster_size") == 1.0
    assert pairwise_recall_estimator(reference, reference, sampling_type="cluster_block", weights="cluster_size") == 1.0
    assert pairwise_recall_estimator(reference, reference, sampling_type="single_block", weights="cluster_size") == 1.0
