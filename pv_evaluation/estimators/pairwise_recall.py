import numpy as np
import pandas as pd
import scipy.special as sp

from ..metrics.utils import validate_membership
from .ratio_estimators import ratio_estimator, std_dev


def pairwise_recall_arrays(prediction, reference, sampling_type, weights):
    validate_membership(prediction)
    validate_membership(reference)

    inner = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner", copy=False)
    vals = inner.groupby(["prediction", "reference"]).size()
    f_sum = vals.to_frame().assign(cmb=sp.comb(vals.values, 2)).groupby("reference").sum().cmb.sort_index().values
    cluster_sizes = inner.reference.value_counts(sort=False).sort_index().values

    if sampling_type == "record":
        if weights == "uniform":
            return (2 *f_sum / cluster_sizes, cluster_sizes - 1)
        elif weights == "cluster_size":
            raise Exception("'cluster_size' weights are not used with 'record' sampling type.")
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "cluster":
        if weights == "uniform":
            return (f_sum, sp.comb(cluster_sizes, 2))
        elif weights == "cluster_size":
            return (2 * f_sum / cluster_sizes, cluster_sizes - 1)
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "single_block":
        TP_block = np.sum(sp.comb(vals.values, 2))
        T_block = np.sum(sp.comb(inner.reference.value_counts(sort=False).values, 2))
        return TP_block / (T_block)
    elif sampling_type == "cluster_block":
        if weights == "uniform":
            N = f_sum
            D = sp.comb(cluster_sizes, 2)
            return (N, D)
        elif weights == "cluster_size":
            N = f_sum / cluster_sizes
            D = sp.comb(cluster_sizes, 2) / cluster_sizes
            return (N, D)
    else:
        raise Exception("Unrecognized 'sampling_type' option. Should be one of 'record', 'cluster', or 'single_block'")



def pairwise_recall_estimator(prediction, reference, sampling_type, weights):
    """Pairwise recall estimates for small non-replacement samples.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for sampled reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.
        sampling_type (str): sampling mechanism used to obtain reference clusters. Should be one of "record", "cluster", or "single_block".
            Note that, for "record" sampling, it is assumed that no two different sampled records had the same associated cluster.
        weights (str): sampling probability weights. Should be one of "uniform" or "cluster_size".

    Returns:
        float: pairwise recall estimate.
    """
    N, D = pairwise_recall_arrays(prediction, reference, sampling_type, weights)
    return ratio_estimator(N, D)


def pairwise_recall_std(prediction, reference, sampling_type, weights):
    N, D = pairwise_recall_arrays(prediction, reference, sampling_type, weights)
    return std_dev(N, D)


