import numpy as np
from scipy.special import comb
import pandas as pd


def cluster_sizes(membership_vect):
    return np.unique(membership_vect, return_counts=True)[1]


def links_count(membership_vect):
    return np.sum(comb(cluster_sizes(membership_vect), 2))


def true_positives(prediction: pd.Series, reference: pd.Series):
    I = np.intersect1d(prediction.index, reference.index)
    TP_cluster_sizes = np.unique((prediction[I], reference[I]), axis=1, return_counts=True)[1]

    return np.sum(comb(TP_cluster_sizes, 2))


def false_positives(prediction, reference):
    return links_count(prediction) - true_positives(prediction, reference)


def raw_precision(prediction, reference):
    return true_positives(prediction, reference) / links_count(prediction)


def raw_recall(pred_labels, true_labels):
    return raw_precision(true_labels, pred_labels)


def raw_precision_recall(pred_labels, true_labels):
    return (raw_precision(pred_labels, true_labels), raw_recall(pred_labels, true_labels))


def raw_fscore(pred_labels, true_labels, beta=1.0):
    P = raw_precision(pred_labels, true_labels)
    R = raw_recall(pred_labels, true_labels)

    return (1 + beta**2) * P * R / (beta**2 * P + R)
