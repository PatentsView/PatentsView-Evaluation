import numpy as np
import pandas as pd
from scipy.special import comb

from .metrics.utils import validate_membership


def ratio_estimator(B, A):
    """Ratio estimator for mean(B)/mean(A)"""
    assert len(A) == len(B)

    A_mean = np.mean(A)
    B_mean = np.mean(B)
    n = len(A)

    adj = 1 + ((n - 1) * A_mean) ** (-1) * np.mean(A * (B / B_mean - A / A_mean))

    return adj * B_mean / A_mean


def pairwise_precision_estimator(prediction, reference, sampling_type, weights):
    """Pairwise precision estimates for small non-replacement samples.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for sampled reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.
        sampling_type (str): Sampling mechanism used to obtain reference clusters. Should be one of "record", "cluster", or "single_block".
            Note that, for "record" sampling, it is assumed that no two different sampled records had the same associated cluster.
        weights (str): Sampling probability weights. Should be one of "uniform" or "cluster_size".

    Returns:
        float: pairwise precision estimate.
    """
    validate_membership(prediction)
    validate_membership(reference)

    inner = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner", copy=False)
    vals = inner.groupby(["prediction", "reference"]).size()
    f_sum = vals.to_frame().assign(cmb=comb(vals.values, 2)).groupby("reference").sum().cmb.sort_index().values
    cluster_sizes = inner.reference.value_counts(sort=False).sort_index().values
    P = np.sum(comb(prediction.value_counts(sort=False).values, 2))

    if sampling_type == "record":
        if weights == "uniform":
            return len(prediction) * np.mean(f_sum / cluster_sizes) / P
        elif weights == "cluster_size":
            raise Exception("'cluster_size' weights are not used with 'record' sampling type.")
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "cluster":
        if weights == "uniform":
            return len(prediction) * ratio_estimator(f_sum, cluster_sizes) / P
        elif weights == "cluster_size":
            return len(prediction) * np.mean(f_sum / cluster_sizes) / P
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "single_block":
        TP_block = np.sum(comb(vals.values, 2))
        P_block = np.sum(comb(inner.prediction.value_counts(sort=False).values, 2))
        I = prediction.isin(inner.prediction)
        A = inner.prediction.value_counts(sort=False).sort_index().values
        B = prediction[I].value_counts(sort=False).sort_index().values
        P_block_minus = np.sum(A * (B - A))
        return TP_block / (P_block + 0.5 * P_block_minus)
    elif sampling_type == "cluster_block":
        if weights == "uniform":
            N = f_sum
            K = prediction.isin(inner.prediction)

            def lambd(x):
                I = inner.prediction.index.isin(x.index)
                J = prediction[K].isin(inner.prediction[I])
                A = inner.prediction[I].value_counts(sort=False).sort_index().values
                B = prediction[K][J].value_counts(sort=False).sort_index().values
                return np.sum(A * (B - A))

            P_minus = inner.groupby("reference").apply(lambd)
            D = f_sum + 0.5 * P_minus
            return ratio_estimator(N, D)
        elif weights == "cluster_size":
            N = f_sum / cluster_sizes
            K = prediction.isin(inner.prediction)

            def lambd(x):
                I = inner.prediction.index.isin(x.index)
                J = prediction[K].isin(inner.prediction[I])
                A = inner.prediction[I].value_counts(sort=False).sort_index().values
                B = prediction[K][J].value_counts(sort=False).sort_index().values
                return np.sum(A * (B - A))

            P_minus = inner.groupby("reference").apply(lambd)
            D = (f_sum + 0.5 * P_minus) / cluster_sizes
            return ratio_estimator(N, D)
    else:
        raise Exception("Unrecognized 'sampling_type' option. Should be one of 'record', 'cluster', or 'single_block'")


def pairwise_recall_estimator(prediction, reference, sampling_type, weights):
    """Pairwise recall estimates for small non-replacement samples.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment.
        reference (Series):  membership vector for sampled reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment.
        sampling_type (str): Sampling mechanism used to obtain reference clusters. Should be one of "record", "cluster", or "single_block".
            Note that, for "record" sampling, it is assumed that no two different sampled records had the same associated cluster.
        weights (str): Sampling probability weights. Should be one of "uniform" or "cluster_size".

    Returns:
        float: pairwise recall estimate.
    """
    validate_membership(prediction)
    validate_membership(reference)

    inner = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner", copy=False)
    vals = inner.groupby(["prediction", "reference"]).size()
    f_sum = vals.to_frame().assign(cmb=comb(vals.values, 2)).groupby("reference").sum().cmb.sort_index().values
    cluster_sizes = inner.reference.value_counts(sort=False).sort_index().values

    if sampling_type == "record":
        if weights == "uniform":
            return 2 * ratio_estimator(f_sum / cluster_sizes, cluster_sizes - 1)
        elif weights == "cluster_size":
            raise Exception("'cluster_size' weights are not used with 'record' sampling type.")
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "cluster":
        if weights == "uniform":
            return ratio_estimator(f_sum, comb(cluster_sizes, 2))
        elif weights == "cluster_size":
            return 2 * ratio_estimator(f_sum / cluster_sizes, cluster_sizes - 1)
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "single_block":
        TP_block = np.sum(comb(vals.values, 2))
        T_block = np.sum(comb(inner.reference.value_counts(sort=False).values, 2))
        return TP_block / (T_block)
    elif sampling_type == "cluster_block":
        if weights == "uniform":
            N = f_sum
            D = comb(cluster_sizes, 2)
            return ratio_estimator(N, D)
        elif weights == "cluster_size":
            N = f_sum / cluster_sizes
            D = comb(cluster_sizes, 2) / cluster_sizes
            return ratio_estimator(N, D)
    else:
        raise Exception("Unrecognized 'sampling_type' option. Should be one of 'record', 'cluster', or 'single_block'")


def std_dev(B, A):
    assert len(A) == len(B)

    A_mean = np.mean(A)
    B_mean = np.mean(B)
    n = len(A)

    return (B_mean / A_mean) * np.sqrt(
        np.sum((A / A_mean) ** 2 + (B / B_mean) ** 2 - 2 * (A * B) / (A_mean * B_mean)) / (n * (n - 1))
    )


def pairwise_precision_std(prediction, reference, sampling_type, weights):
    validate_membership(prediction)
    validate_membership(reference)

    inner = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner", copy=False)
    vals = inner.groupby(["prediction", "reference"]).size()
    f_sum = vals.to_frame().assign(cmb=comb(vals.values, 2)).groupby("reference").sum().cmb.sort_index().values
    cluster_sizes = inner.reference.value_counts(sort=False).sort_index().values
    P = np.sum(comb(prediction.value_counts(sort=False).values, 2))

    if sampling_type == "record":
        if weights == "uniform":
            return len(prediction) / P * np.std(f_sum / cluster_sizes)
        elif weights == "cluster_size":
            raise Exception("'cluster_size' weights are not used with 'record' sampling type.")
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "cluster":
        if weights == "uniform":
            return len(prediction) * std_dev(f_sum, cluster_sizes) / P
        elif weights == "cluster_size":
            return len(prediction) * np.std(f_sum / cluster_sizes) / P
        else:
            raise Exception("Unrecognized 'weight' option. Should be one of 'uniform' or 'cluster_size'.")
    elif sampling_type == "single_block":
        return np.nan
    elif sampling_type == "cluster_block":
        if weights == "uniform":
            raise NotImplementedError()
        elif weights == "cluster_size":
            N = f_sum / cluster_sizes
            K = prediction.isin(inner.prediction)

            def lambd(x):
                I = inner.prediction.index.isin(x.index)
                J = prediction[K].isin(inner.prediction[I])
                A = inner.prediction[I].value_counts(sort=False).sort_index().values
                B = prediction[K][J].value_counts(sort=False).sort_index().values
                return np.sum(A * (B - A))

            P_minus = inner.groupby("reference").apply(lambd)
            D = (f_sum + 0.5 * P_minus) / cluster_sizes
            return std_dev(N, D)
    else:
        raise Exception("Unrecognized 'sampling_type' option. Should be one of 'record', 'cluster', or 'single_block'")
