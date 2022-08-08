import numpy as np
import pandas as pd

from pv_evaluation.metrics.utils import validate_membership
from pv_evaluation.estimators.ratio_estimators import ratio_estimator, std_dev


def cluster_recall_arrays(prediction, reference, sampling_type, weights):
    """Raw data for use with ratio estimator and standard deviation estimators."""
    validate_membership(prediction)
    validate_membership(reference)

    inner = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner")
    if sampling_type == "cluster_block":
        if weights == "uniform":
            N = inner.groupby("reference").nunique()["prediction"] == 1
            D = np.ones(len(N))

            return (N, D)
        elif weights == "cluster_size":
            (N, D) = cluster_recall_arrays(prediction, reference, sampling_type="cluster_block", weights="uniform")
            cluster_sizes = inner.reference.value_counts(sort=False).values

            return (N / cluster_sizes, D / cluster_sizes)
    elif sampling_type == "single_block":
        N = [np.mean(inner.nunique()["prediction"] == 1)]
        D = [1]
        return (N, D)
    else:
        raise Exception("Unrecognized 'sampling_type' option. Should be 'cluster_block'.")


def cluster_recall_estimator(prediction, reference, sampling_type="cluster_block", weights="cluster_size"):
    """Cluster recall estimates.

    The only sampling mechanism considered is:

        * **cluster_block** sampling: ground truth clusters are directly sampled and treated as block samples.

    The following probability weights can be used:

        * **uniform**: uniform probability weights.
        * **cluster_size**: probability weights proportional to cluster size.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for sampled reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.
        sampling_type (str): sampling mechanism used to obtain reference clusters. Should be "cluster_block".
            Note that, for "record" sampling, it is assumed that no two different sampled records had the same associated cluster.
        weights (str): sampling probability weights. Should be one of "uniform" or "cluster_size".

    Returns:
        float: cluster recall estimate.

    Notes:
        * We recommend using the **cluster_block** estimator when possible since it is the most efficient.
        * This is meant for use with relatively small non-replacement samples.
        * For unknown sampling processes, the **single_block** estimator can be used.
    """
    N, D = cluster_recall_arrays(prediction, reference, sampling_type, weights)
    return ratio_estimator(N, D)


def cluster_recall_std(prediction, reference, sampling_type="cluster_block", weights="cluster_size"):
    """Standard deviation estimates for the pairwise recall estimator."""
    N, D = cluster_recall_arrays(prediction, reference, sampling_type, weights)
    return std_dev(N, D)
