import dill as pickle
import numpy as np
import pandas as pd
import os
import tempfile
import plotly.express as px
from .utils import read_auto


class DisambiguationSummary:
    def __init__(self, datapath, name=None, processed_data_dir=None):
        """Report disambiguation summaries. Object instantiation is used to manage data pre-processing and speed up some of the computations.

        Args:
            datapath (str): Path to the disambiguation data (csv, tsv or parquet format).
                The data should have four columns: "patent_id", "inventor_id", "name_first", and "name_last".
            processed_data_dir (str, optional): Path to a directory where to store processed data.
                Data from past runs will be re-used if it is found in this directory.
                Defaults to None for a temporary directory.
            name (str): Name of the disambiguation algorithm to show in plots.n
        """
        if name is None:
            raise Exception("Name is required to read/save processed data file ")
        self.name = name
        self.processed_data_dir = processed_data_dir
        if self.processed_data_dir is None:
            self.processed_data_dir = tempfile.mkdtemp()
            self.tempdir = self.processed_data_dir

        self._data: pd.DataFrame = read_auto(datapath)
        self._validate_data()

        # Lazy initialization
        self._cluster_size_distribution = None
        self._cluster_unique_name_distribution = None
        self._homonymy_rate_distribution = None
        self.id_field = None
        self.record_id_field = 'patent_id'

    def _validate_data(self):
        raise NotImplementedError()

    def __save__(self):
        if self.processed_data_dir is not None:
            filename = "processed_{name}_disambiguation_data.pkl".format(name=self.name)
            filepath = os.path.join(self.processed_data_dir, filename)
            with open(filepath, "wb") as pfile:
                pickle.dump(obj=self, file=pfile, protocol=pickle.HIGHEST_PROTOCOL)

    def get_cluster_size_distribution(self):
        """Get the cluster size distribution summary.

        Returns:
            Series: Series of cluster sizes value counts
        """
        if self._cluster_size_distribution is None:
            self._cluster_size_distribution = (
                self.get_cluster_sizes_dd()["Number of records"]
                    .value_counts()
                    .reset_index()
                    .rename(columns={"Number of records": "Number of clusters", "index": "Number of records"})
            )

        return self._cluster_size_distribution.copy()

    def get_cluster_sizes_dd(self):
        """Return the number of records per disambiguated cluster as a Dask DataFrame.

        The mode of the cluster members' data label are kept in the resulting dataframe.
        """
        return (
            self._data.groupby(self.id_field)
            .agg({self.record_id_field: "count", "data_label": "first"})
            .rename(columns={self.record_id_field: "Number of records"})
        )

    def plot_cluster_size_distribution(self, range=(0, 20)):
        """Plot the distribution of the number of records per cluster

        Args:
            range (tuple, optional): x-axis limits (inclusive range for the number of record by cluster). Defaults to (1, 10).

        Returns:
            Plotly graph object.
        """
        data = self.get_cluster_size_distribution().reset_index()
        fig = px.bar(
            data, x="Number of records", y="Number of clusters",
            title="Distribution of the number of records per cluster",
        )
        fig.update_xaxes(range=range)

        data_range = data["Number of clusters"][data["Number of records"].between(range[0], range[1])]
        ylim = 0
        if data_range.size > 1:
            ylim = max(data_range)
        fig.update_yaxes(range=(0, ylim), autorange=False)

        fig.update_traces(name=self.name)
        return fig

    def get_top_clusters(self, n=10):
        """Get DataFrame of n most prolific clusters (by number of records)

        Args:
            n (int, optional): Number of clusters to return. Defaults to 10.

        Returns:
            DataFrame containing the sorted top n most prolific clusters.
        """
        return self.get_cluster_sizes_dd().sort_values(by="Number of records", ascending=False).head(n)

    def entropy_curve(self, q_range=np.linspace(0, 2)):
        data = self.get_cluster_size_distribution()
        data["Number of clusters"] = data["Number of clusters"] / sum(data["Number of clusters"])

        def hill_number(arr, q):
            if q == 1:
                I = arr > 0
                return np.exp(-np.sum(arr[I] * np.log(arr[I])))
            elif q == 0:
                return np.sum(arr > 0)
            else:
                return np.sum(arr ** (q)) ** (1 / (1 - q))

        return [hill_number(data["Number of clusters"], q) for q in q_range], q_range

    def plot_entropy_curve(self, q_range=np.linspace(0, 2)):
        ent, q = self.entropy_curve(q_range)
        fig = px.line(x=q, y=ent, title="Hill Numbers entropy curve", labels={"x": "q", "y": "Entropy"})
        fig.update_traces(name=self.name)
        return fig

    def get_cluster_unique_name_distribution(self):
        """Get the proportion of homogeneous clusters (no name variation) by cluster size."""
        if self._cluster_unique_name_distribution is None:
            self._cluster_unique_name_distribution = (
                self.get_cluster_sizes_dd()
                .join(
                    self._data.groupby(self.id_field)["data_label"]
                    .apply(lambda x: len(set(x)) == 1)
                    .rename("Proportion of unique name")
                )
                    .groupby("Number of records")
                    .agg({"Proportion of unique name": "mean"})
                    .reset_index()
            )

        return self._cluster_unique_name_distribution.copy()

    def plot_cluster_unique_name_distribution(self, range=(0, 100)):
        """Plot the proportion of homogeneous clusters (no name variation) by cluster size."""
        data = self.get_cluster_unique_name_distribution()
        fig = px.bar(
            data,
            x="Number of records",
            y="Proportion of unique name",
            title="Proportion of homogeneous clusters (no name variation) by cluster size",
        )
        fig.update_xaxes(range=range)

        ylim = max(data["Proportion of unique name"][data["Number of records"].between(range[0], range[1])])
        fig.update_yaxes(range=(0, ylim), autorange=False)

        fig.update_traces(name=self.name)
        return fig

    def get_homonymy_rate_distribution(self):
        """Get homonymy rates by cluster size.

        The homonymy rate is the proportion of clusters which share at least one name mention with another cluster.
        """
        if self._homonymy_rate_distribution is None:
            data = self._data
            data = self._data.assign(id_2=data.index, homophones=data.data_label)

            dat = (
                data.join(
                    data.groupby("homophones")["id_2"].apply(lambda x: len(set(x)) > 1).rename("Shared name"),
                    on="homophones",
                )[["Shared name", "id_2", self.record_id_field]]
                .groupby("id_2")
                    .agg({self.record_id_field: "count", "Shared name": "sum"})
            )

            dat = dat.assign(shared_name_prop=np.where(dat["Shared name"].values > 1, 1, 0))
            result = dat.groupby(self.record_id_field)["shared_name_prop"].agg(np.mean)

            self._homonymy_rate_distribution = (
                result
                    .reset_index()
                    .rename(columns={"shared_name_prop": "Homonymy rate", self.record_id_field: "Number of records"})
            )

        return self._homonymy_rate_distribution.copy()

    def plot_homonymy_rate_distribution(self, range=(0, 100)):
        """Plot homonymy rate by cluster size.

        The homonymy rate is the proportion of clusters which share at least one name mention with another cluster.
        """
        data = self.get_homonymy_rate_distribution().reset_index()
        fig = px.bar(data, x="Number of records", y="Homonymy rate", title="Homonymy rate by cluster size", )
        fig.update_xaxes(range=range)

        ylim = max(data["Homonymy rate"][data["Number of records"].between(range[0], range[1])])
        fig.update_yaxes(range=(0, ylim), autorange=False)

        fig.update_traces(name=self.name)
        return fig
