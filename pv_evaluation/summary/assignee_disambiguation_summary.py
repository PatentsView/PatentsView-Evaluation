from itertools import combinations
import pandas as pd

from pv_evaluation.summary.utils import EuclideanDistance, DistanceMetric, calculate_silhouette_a_i, calculate_silhouette_b_i
from pv_evaluation.summary.disambiguation_summary import DisambiguationSummary


class AssigneeDisambiguationSummary(DisambiguationSummary):
    def __init__(self, datapath, name):
        super().__init__(datapath, name, id_field="assignee_id")

        # placeholder for storing various distances
        self.intra_cluster_distances = {}
        self.inter_cluster_distances = {}
        self.intra_point_distances = {}
        self.dataset_inter_cluster_distance = None
        self.cluster_diameters = {}

    def get_intra_cluster_distance(self, *args, **kwargs):
        cluster_name = None
        if len(args) > 1:
            cluster_name = args[0]
        cluster_name = kwargs.get("cluster_name", cluster_name)
        if cluster_name is not None:
            return self.intra_cluster_distances.get(cluster_name, None)
        else:
            return self.intra_cluster_distances

    def get_inter_cluster_distance(self, cluster_name1, cluster_name2):
        distance = self.inter_cluster_distances.get((cluster_name1, cluster_name2), None)
        if distance is None:
            distance = self.inter_cluster_distances.get((cluster_name1, cluster_name2), None)
        return distance

    def get_dataset_inter_cluster_distance(self):
        return self.dataset_inter_cluster_distance

    def collect_intra_cluster_distance(self, distance_metric=EuclideanDistance()):
        """
        Collects the within-cluster distance for all clusters in the dataset
        Args:
            distance_metric (DistanceMetric): An object representing the type of distance measure to use to calculate distance. (Euclidean or Correlation). Default: Euclidean
        """
        for cluster_name in self._data.cluster_label.unique():
            mention_names = self._data[self._data.cluster_label == cluster_name].data_label
            points_generator = combinations(mention_names, r=2)
            try:
                mean_distance, pointwise_distances = distance_metric.multi_point_distance(points_generator)
                self.intra_cluster_distances[cluster_name] = (mean_distance, pointwise_distances)
                self.cluster_diameters[cluster_name] = max(pointwise_distances.values())

            except ZeroDivisionError:
                self.intra_cluster_distances[cluster_name] = None

    def collect_inter_cluster_distance(
        self, distance_metric: DistanceMetric = EuclideanDistance(), measure_using: str = "centroid"
    ):
        """
        Collects all the between-cluster distance between all cluster in datasets.
        Args:
            distance_metric: An object representing the type of distance measure to use to calculate distance. (Euclidean or Correlation)
            measure_using: Cluster comparison mechanism. 'centroid' or 'members'.

        Returns:
            float: Inter-cluster distance
        """
        cluster_names = self._data.cluster_label.unique()
        if measure_using != "centroid":
            raise NotImplementedError
        points_generator = combinations(cluster_names, 2)
        try:
            self.dataset_inter_cluster_distance, self.inter_cluster_distances = distance_metric.multi_point_distance(
                points_generator
            )
        except ZeroDivisionError:
            raise Exception("There is only one cluster in the dataset")

    def calculate_silhouette_score(self):
        """
        Calculate silhouette score for all records in the dataset. https://en.wikipedia.org/wiki/Silhouette_(clustering)
        Calculate the silhouette score formula: s(i) = b(i) - a(i) / max {a(i), b(i)} where i = current record

        """
        silhouette_scores = {}
        for record_idx in self._data.index:
            record_cluster_label = self._data.loc[record_idx, "cluster_label"]
            record_label = self._data.loc[record_idx, "data_label"]
            current_cluster_distances = self.intra_cluster_distances[record_cluster_label]
            # s(i) = 0 if |C] =1
            if current_cluster_distances is None:
                silhouette_scores[record_idx] = 0
            else:
                a = calculate_silhouette_a_i(record_label, current_cluster_distances[1])
                b = calculate_silhouette_b_i(record_cluster_label, self._data.cluster_label.tolist())
                silhouette_scores[record_idx] = (b - a) / max(a, b)

        # Update the _data variable with calculated scores
        silhouette_series = pd.DataFrame(silhouette_scores.values(), index=silhouette_scores.keys())
        silhouette_series.rename({0: "sihouette_score"}, axis=1, inplace=True)
        self._data = self._data.join(silhouette_series)
