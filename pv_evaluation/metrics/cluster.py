"""Cluster performance metrics.
"""
import numpy as np
import pandas as pd
import sklearn.metrics as sm
from functools import wraps

from pv_evaluation.metrics.utils import validate_membership


def clusters_count(membership_vect):
    """Compute number of clusters for a given membership vector.

    Args:
        membership_vect (Series): membership vector, i.e. a pandas Series indexed by mention ids and with values representing cluster assignment.

    Returns:
        int: number of clusters
    """
    validate_membership(membership_vect)

    return membership_vect.nunique()


def cluster_precision(prediction, reference):
    """Compute cluster precision, i.e. the proportion of predicted clusters with no erroneous assignment.

    A cluster makes an erroneous assignment if it contains two mention ids that are not part of the same reference cluster.

    A perfect cluster precision means that all predicted links are correct.

    Notes:
        * The prediction and reference membership vectors are inner joined before cluster precision is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: cluster precision
    """
    validate_membership(prediction)
    validate_membership(reference)

    data = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner", copy=False)
    n_correct_clusters = np.sum(data.groupby(["prediction"]).nunique()["reference"].values == 1)

    return n_correct_clusters / clusters_count(data.prediction)


def cluster_recall(prediction, reference):
    """Compute cluster recall, i.e. the proportion of reference clusters that are not split accross different predicted clusters.

    A perfect cluster recall means that all reference links are correctly predicted.

    Notes:
        * The prediction and reference membership vectors are inner joined before cluster recall is computed.
        * This is the same as `cluster_precision(reference, prediction)`_.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: cluster recall
    """
    return cluster_precision(reference, prediction)


def cluster_precision_recall(prediction, reference):
    """Cluster precision and cluster recall tuple.

    Notes:
        * The prediction and reference membership vectors are inner joined before metrics are computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        tuple: (cluster precision, cluster recall)
    """
    return (cluster_precision(prediction, reference), cluster_recall(prediction, reference))


def cluster_fscore(prediction, reference, beta=1.0):
    """F-score between cluster precision and cluster recall.

    This is indexed by a parameter `beta` representing the statement that "recall is beta times more important than precision".
    See [this Wikipedia article](https://en.wikipedia.org/wiki/F-score) for more information.

    For beta = 1 (default value), this is the harmonic mean between precision and recall.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.
        beta (float, optional): weight. Defaults to 1.0.

    Returns:
        float: f-score
    """

    P = cluster_precision(prediction, reference)
    R = cluster_recall(prediction, reference)

    return (1 + beta**2) * P * R / (beta**2 * P + R)


def cluster_fowlkes_mallows(prediction, reference):
    """Geometric mean between cluster precision and cluster recall.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: geometric mean between cluster precision and cluster recall.
    """
    P = cluster_precision(prediction, reference)
    R = cluster_recall(prediction, reference)

    return np.sqrt(P * R)


def wrap_sklearn_metric(sklearn_metric):
    """Generic function to wrap sklearn cluster metrics.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        sklearn_metric (function): cluster metric to wrap.
    """

    @wraps(sklearn_metric)
    def func(prediction, reference, **kw):
        validate_membership(prediction)
        validate_membership(reference)

        data = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner", copy=False)
        prediction_codes = pd.Categorical(data.prediction).codes.astype(np.int64)
        reference_codes = pd.Categorical(data.reference).codes.astype(np.int64)

        return sklearn_metric(reference_codes, prediction_codes, **kw)

    return func


def cluster_homogeneity(prediction, reference):
    """Cluster homogeneity score (based on conditional entropy).

    This wraps scikit-learn's `homogeneity score function <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html>`.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: homogeneity score
    """
    return wrap_sklearn_metric(sm.homogeneity_score)(prediction, reference)


def cluster_completeness(prediction, reference):
    """Cluster completeness score (based on conditional entropy)

    This wraps scikit-learn's `completeness score function <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html>`.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: completeness score
    """
    return wrap_sklearn_metric(sm.completeness_score)(prediction, reference)


def cluster_v_measure(prediction, reference, beta=1.0):
    """Compute the V-measure.

    This wraps scikit-learn's `V-measure function <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn-metrics-v-measure-score>`.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: V-measure
    """

    return wrap_sklearn_metric(sm.v_measure_score)(prediction, reference, beta=beta)


def rand_score(prediction, reference):
    """Compute the Rand index.

    This wraps scikit-learn's `rand index function <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#sklearn.metrics.rand_score>`.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: rand index
    """
    return wrap_sklearn_metric(sm.rand_score)(prediction, reference)


def adjusted_rand_score(prediction, reference):
    """Compute the adjusted Rand index.

    This wraps scikit-learn's `adjusted rand score function <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn-metrics-adjusted-rand-score>`.

    Notes:
        * The prediction and reference membership vectors are inner joined before this metric is computed.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.

    Returns:
        float: adjusted rand index
    """

    return wrap_sklearn_metric(sm.adjusted_rand_score)(prediction, reference)
