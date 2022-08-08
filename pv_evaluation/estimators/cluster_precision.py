import numpy as np
import pandas as pd

from pv_evaluation.metrics.utils import validate_membership
from pv_evaluation.estimators.ratio_estimators import ratio_estimator, std_dev


def cluster_precision_arrays(prediction, reference, sampling_type, weights):
    """Raw data for use with ratio estimator and standard deviation estimators."""
    validate_membership(prediction)
    validate_membership(reference)

    inner = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner")
    K = prediction.isin(inner.prediction)
    outer = pd.concat({"prediction": prediction[K], "reference": reference}, join="outer", axis=1)
    pred_count = outer.groupby("reference").nunique(dropna=False)["prediction"]

    contained_within_sample = outer.groupby("prediction").nunique(dropna=False) == 1
    number_contained_by_reference = (
        inner.merge(contained_within_sample, on="prediction").query("reference_y == True").groupby("reference_x").nunique()
    )
    data = pd.concat(
        {"pred_count": pred_count, "n_contained": number_contained_by_reference["prediction"]}, join="outer", axis=1
    )
    data.n_contained = data.n_contained.fillna(0)

    if sampling_type == "cluster_block":
        if weights == "uniform":
            N = data.n_contained
            D = 0.5 * (N + data.pred_count)

            return (N, D)
        elif weights == "cluster_size":
            (N, D) = cluster_precision_arrays(prediction, reference, sampling_type="cluster_block", weights="uniform")
            cluster_sizes = inner.reference.value_counts(sort=False).values

            return (N / cluster_sizes, D / cluster_sizes)
    elif sampling_type == "single_block":
        pred_count = outer.nunique(dropna=False)["prediction"]

        contained_within_sample = outer.groupby("prediction").nunique(dropna=False) == 1
        number_contained = inner.merge(contained_within_sample, on="prediction").query("reference_y == True").nunique()

        N = [np.sum(number_contained)]
        D = [np.sum(0.5 * (N + pred_count))]

        return (N, D)
    else:
        raise Exception("Unrecognized 'sampling_type' option. Should be one of 'cluster_block' or 'single_block'.")


def cluster_precision_estimator(prediction, reference, sampling_type="cluster_block", weights="cluster_size"):
    """Cluster precision estimates.

    The only sampling mechanism considered is:

        * **cluster_block** sampling: ground truth clusters are directly sampled and treated as block samples.

    The following probability weights can be used:

        * **uniform**: uniform probability weights.
        * **cluster_size**: probability weights proportional to cluster size.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for sampled reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.
        sampling_type (str): sampling mechanism used to obtain reference clusters. Should be one of 'cluster_block' or 'single_block'.
            Note that, for "record" sampling, it is assumed that no two different sampled records had the same associated cluster.
        weights (str): sampling probability weights. Should be one of "uniform" or "cluster_size".

    Returns:
        float: cluster precision estimate.

    Notes:
        * This is meant for use with relatively small non-replacement samples.
    """
    N, D = cluster_precision_arrays(prediction, reference, sampling_type, weights)
    return ratio_estimator(N, D)


def cluster_precision_std(prediction, reference, sampling_type="cluster_block", weights="cluster_size"):
    """Standard deviation estimates for the cluster precision estimator."""
    N, D = cluster_precision_arrays(prediction, reference, sampling_type, weights)
    return std_dev(N, D)
