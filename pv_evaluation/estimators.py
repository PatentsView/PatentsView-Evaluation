import numpy as np
import pandas as pd
from scipy.special import comb

from .metrics.utils import validate_membership

def pairwise_precision_estimator(prediction, reference, sampling_type=["record", "cluster", "single_block"], weights=["uniform", "cluster_size"]):
    """Pairwise precision estimates for small non-replacement samples.
    
    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for sampled reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
        sampling_type (list, optional): Sampling mechanism used to obtain reference clusters. Should be one of "record", "cluster", or "single_block". 
            Note that, for "record" sampling, it is assumed that no two different sampled records had the same associated cluster. 
        weights (list, optional): Sampling probability weights. Should be one of "uniform" or "cluster_size".
        
    Returns:
        float: pairwise precision estimate.
    """
    validate_membership(prediction)
    validate_membership(reference)
    
    inner = pd.concat({"prediction":prediction, "reference":reference}, axis=1, join="inner", copy=False)
    vals = inner.groupby(["prediction", "reference"]).size()
    f_sum = vals.to_frame().assign(cmb=comb(vals.values, 2)).groupby("reference").sum().cmb
    cluster_sizes = inner.reference.value_counts(sort=False).values
    P = np.sum(comb(prediction.value_counts(sort=False).values, 2))

    if sampling_type == "record":
        if weights == "uniform":
            return len(prediction) * np.mean(f_sum / cluster_sizes) / P
        if weights == "cluster_size":
            raise Exception("'cluster_size' weights are not used with 'record' sampling type.") 
    elif sampling_type == "cluster":
        if weights == "uniform":
            return len(prediction) * np.mean(f_sum) / np.mean(cluster_sizes) / P
        elif weights == "cluster_size":
            return len(prediction) * np.mean(f_sum / cluster_sizes) / P
    elif sampling_type == "single_block":
        TP_block = np.sum(comb(vals.values, 2))
        P_block = np.sum(comb(inner.prediction.value_counts(sort=False).values, 2))
        I = prediction.isin(inner.prediction)
        P_block_plus = np.sum(comb(prediction[I].value_counts(sort=False).values, 2))
        return 2 * TP_block / (P_block + P_block_plus)
    else:
        raise Exception("Unrecognized 'sampling_type' option. Should be one of 'record', 'cluster', or 'single_block'")
