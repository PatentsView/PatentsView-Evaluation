"""Pairwise link-based classification metrics.
"""

import numpy as np
from scipy.special import comb
import pandas as pd
from .utils import validate_membership


def cluster_sizes(membership_vect):
    """Get cluster sizes for a given membership vector.

    Args:
        membership_vect (Series):  membership vector, i.e. a pandas Series indexed by mention ids and with values representing cluster assignment. 

    Returns:
        Series: cluster sizes
    """
    validate_membership(membership_vect)

    return membership_vect.value_counts(sort=False).values


def links_count(membership_vect):
    """Number of links associated with a given membership vector.
    
    There is one link for each distinct pair of elements within the same cluster.

    Args:
        membership_vect (Series):  membership vector, i.e. a pandas Series indexed by mention ids and with values representing cluster assignment. 
        
    Returns:
        int: number of links
    """
    return np.sum(comb(cluster_sizes(membership_vect), 2))


def true_positives_count(prediction, reference):
    """Number of true positives for given predicted and reference clusterings.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
            

    Returns:
        int: Number of true positives.
    """
    validate_membership(prediction)
    validate_membership(reference)

    data = pd.concat({"prediction": prediction, "reference": reference}, axis=1, join="inner", copy=False)
    TP_cluster_sizes = data.groupby(["prediction", "reference"]).size().values

    return np.sum(comb(TP_cluster_sizes, 2))


def false_positives_count(prediction, reference):
    """Number of false positives for given predicted and reference clusterings.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
            

    Returns:
        int: Number of false positives
    """
    return links_count(prediction) - true_positives_count(prediction, reference)


def pairwise_precision(prediction, reference):
    """Pairwise precision: number of correct links divided by the number of predicted links.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
            
    Returns:
        float: pairwise precision
    """
    return true_positives_count(prediction, reference) / links_count(prediction)


def pairwise_recall(prediction, reference):
    """Pairwise recall: number of correct links divided by the number of reference links.

    This is the same as `pairwise_precision(reference, prediction)`.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
            
    Returns:
        float: pairwise recall
    """

    return pairwise_precision(reference, prediction)


def pairwise_precision_recall(prediction, reference):
    """Pairwise precision and recall

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
            
    Returns:
        tuple: tuple (precision, recall).
    """
    return (pairwise_precision(prediction, reference), pairwise_recall(prediction, reference))


def pairwise_fscore(prediction, reference, beta=1.0):
    """Pairwise precision-recall f-score.

    This is indexed by a parameter `beta` representing the statement that "recall is beta times more important than precision".
    See [this Wikipedia article](https://en.wikipedia.org/wiki/F-score) for more information.
    
    For beta = 1 (default value), this is the harmonic mean between precision and recall.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
        beta (float): weight. Defaults to 1.0.
    
    Returns:
        float: f-score
    """
    P = pairwise_precision(prediction, reference)
    R = pairwise_recall(prediction, reference)

    return (1 + beta ** 2) * P * R / (beta ** 2 * P + R)


def pairwise_fowlkes_mallows(prediction, reference):
    """Geometric mean between pairwise precision and recall.
    
    See [this Wikipedia article](https://en.wikipedia.org/wiki/Fowlkes%E2%80%93Mallows_index) for more information.

    Args:
        prediction (Series):  membership vector for predicted clusters, i.e. a pandas Series indexed by mention ids and with values representing predicted cluster assignment. 
        reference (Series):  membership vector for reference clusters, i.e. a pandas Series indexed by mention ids and with values representing reference cluster assignment. 
            
    Returns:
        float: Fowlks-Mallows index
    """
    P = pairwise_precision(prediction, reference)
    R = pairwise_recall(prediction, reference)

    return np.sqrt(P * R)
