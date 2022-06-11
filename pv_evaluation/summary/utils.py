import math
import os

import dask.dataframe as dd
import editdistance
import pandas as pd


def read_auto(datapath) -> dd.DataFrame:
    _, ext = os.path.splitext(datapath)

    if ext == ".csv":
        return dd.read_csv(datapath)
    elif ext == ".tsv":
        return dd.read_csv(datapath, sep="\t")
    elif ext in [".parquet", ".pq", ".parq"]:
        return dd.read_parquet(datapath)
    else:
        raise Exception("Unsupported file type. Should be one of csv, tsv, or parquet.")


class DistanceMetric():
    def pairwise_distance(self, point1, point2):
        """

        Args:
            point1:  distance from this data point (organization/person name)
            point2:  distance to this data point  (organization/person name)

        Returns:
            int: Distance
        """
        raise NotImplementedError

    def multi_point_distance(self, points_generator):
        """
        Args:
            points_generator:

        Returns:

        """
        raise NotImplementedError


class EuclideanDistance(DistanceMetric):

    def pairwise_distance(self, point1: str, point2: str):
        """
        Levenshtein distance between two points.

        Args:
            point1:  distance from this data point (organization/person name)
            point2:  distance to this data point  (organization/person name)

        Returns:
            int: Levenshtein edit distance
        """
        return editdistance.distance(standardize_names(point1), standardize_names(point2))

    def multi_point_distance(self, points_generator):
        """
        Calculates Euclidean distance between a set of points. Calculate  1/n * ∑( x - y )^2


        Args:
            points_generator: python generator that provides pair of points (tuples) for which the distance needs to be calculated

        Returns: tuple of euclidean distance and dictionary of pairwise distances

        """
        x_y_count = 0
        distance = 0
        distances = {}
        for point1, point2 in points_generator:
            current_distance = self.pairwise_distance(point1, point2)
            distances[(point1, point2)] = current_distance
            distance += math.pow(current_distance, 2)
            x_y_count += 1
        return distance / x_y_count, distances


class CorrelationDistance(DistanceMetric):
    """

    Args:
        point1:  distance from this data point (organization/person name)
        point2:  distance to this data point  (organization/person name)

    Returns:
        int: Correlation Distance
    """

    def __init__(self):
        super(CorrelationDistance, self).__init__()
        self.data_frame = None
        self.data_matrix = None

    def multi_point_distance(self, points_generator):
        raise NotImplementedError
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer()

    def pairwise_distance(self, point1: object, point2: object):
        raise NotImplementedError


def standardize_names(name: str, *args, **kwargs):
    """
    String standardization helper

    Args:
        name: name to be standardized
        *args:
        **kwargs: Supported boolean options with defaults: lower(True), trim_whitespace(True), strip_extra_whitespace(True), force_ascii(False).

    Returns: standardized string

    """
    processed_name = name
    if kwargs.get('lower', True):
        processed_name = processed_name.lower()
    if kwargs.get('trim_whitespace', True):
        processed_name.strip()
    if kwargs.get('strip_extra_whitespace', True):
        import re
        processed_name = re.sub('(\s){2,}', '\\1', processed_name)
    if kwargs.get('force_ascii', False):
        processed_name = processed_name.encode('ascii', 'ignore')
    return processed_name


def calculate_silhouette_a_i(record_id, current_cluster_distances):
    """
    Calculate the 'dissimilarity' component (a) of the silhouette score for the current record
    i.e the measure of dissimilarity of current record with all other records in its cluster
    a(i) = [ ∑ pairwise_distance(i, j)] / no. of. other data points in cluster
    j  = data points in record's cluster

    Args:
        record_id: Record for which silhouette score is being calculated
        current_cluster_distances: Intra cluster distances between all records in the cluster that the current record belongs to.

    Returns:
        mean dissimilarity for the record (float)
    """
    total_distance = 0
    total_comparisons = 0
    for point1, point2 in current_cluster_distances:
        if point1 == record_id or point2 == record_id:
            total_distance += current_cluster_distances[(point1, point2)]
            total_comparisons += 1
    return total_distance / total_comparisons


def calculate_silhouette_b_i(record_cluster_label, cluster_labels, distance_metric=EuclideanDistance()):
    """
    Calculate the modified 'similarity' component (b) of the silhouette score for current record
    i.e the measure of similarity of current record with all clusters, except its own,  in the dataset
    b(i) = min([ ∑ pairwise_distance(i, j)] / no. of. cluster in dataset - 1)
    j  = cluster centroid

    Args:
        distance_metric: Distance metric to use to calculate distance. Defaults to Euclidean
        record_cluster_label: Cluster centroid of the cluster in which the current record belongs to
        cluster_labels: Centroids of all other clusters in the dataset

    Returns:
        lowest of the mean similarities for the record (float) with all the other clusters
    """

    distance_comparison_points = zip(record_cluster_label, [cluster_name for cluster_name in cluster_labels if
                                                            cluster_name != record_cluster_label])
    return min(distance_metric.multi_point_distance(distance_comparison_points)[1].values())
