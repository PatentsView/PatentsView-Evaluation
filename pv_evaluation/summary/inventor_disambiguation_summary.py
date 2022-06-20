import numpy as np
import pandas as pd
import os
import plotly.express as px


def read_auto(datapath):
    _, ext = os.path.splitext(datapath)

    if ext == ".csv":
        return pd.read_csv(datapath)
    elif ext == ".tsv":
        return pd.read_csv(datapath, sep="\t")
    elif ext in [".parquet", ".pq", ".parq"]:
        return pd.read_parquet(datapath)
    else:
        raise Exception("Unsupported file type. Should be one of csv, tsv, or parquet.")


class InventorDisambiguationSummary:
    def __init__(self, datapath, name=None):
        """Report inventor disambiguation summaries.

        Args:
            datapath (str): Path to the inventor disambiguation data (csv, tsv or parquet format).
                The data should have four columns: "patent_id", "inventor_id", "name_first", and "name_last".
            name (str): Name of the disambiguation algorithm to show in plots. Defaults to the provided datapath.
        """
        self.name = datapath if name is None else name

        self._data = read_auto(datapath)
        self._validate_data()

        # Lazy initialization
        self._cluster_size_distribution = None
        self._cluster_unique_name_distribution = None
        self._homonymy_rate_distribution = None

    def _validate_data(self):
        for col in ["patent_id", "inventor_id", "name_first", "name_last"]:
            assert (col in self._data.columns) or (col in [self._data.index.name]), f"{col} is not in the data columns."

    def get_cluster_size_distribution(self):
        """Get the cluster size distribution summary.

        Returns:
            Series: Series of cluster sizes value counts
        """
        if self._cluster_size_distribution is None:
            self._cluster_size_distribution = (
                self.get_cluster_sizes_dd()["Number of patents"]
                .value_counts()
                .reset_index()
                .rename(columns={"Number of patents": "Number of inventors", "index": "Number of patents"})
            )

        return self._cluster_size_distribution.copy()

    def get_cluster_sizes_dd(self):
        """Return the number of patents per disambiguated inventor as a Dask DataFrame.

        The mode of the inventor's first name and last name are kept in the resulting dataframe.
        """
        return (
            self._data.groupby("inventor_id")
            .agg({"patent_id": "count", "name_first": "first", "name_last": "first"})
            .rename(columns={"patent_id": "Number of patents"})
        )

    def plot_cluster_size_distribution(self, range=(0, 20)):
        """Plot the distribution of the number of patents per inventor

        Args:
            range (tuple, optional): x-axis limits (inclusive range for the number of patents by inventor). Defaults to (1, 10).

        Returns:
            Plotly graph object.
        """
        data = self.get_cluster_size_distribution().reset_index()
        fig = px.bar(
            data,
            x="Number of patents",
            y="Number of inventors",
            title="Distribution of the number of patents per inventor",
        )
        fig.update_xaxes(range=range)

        ylim = max(data["Number of inventors"][data["Number of patents"].between(range[0], range[1])])
        fig.update_yaxes(range=(0, ylim), autorange=False)

        fig.update_traces(name=self.name)
        return fig

    def get_top_inventors(self, n=10):
        """Get DataFrame of n most prolific inventors

        Args:
            n (int, optional): Number of inventors to return. Defaults to 10.

        Returns:
            DataFrame containing the sorted top n most prolific inventors.
        """
        return self.get_cluster_sizes_dd().sort_values(by="Number of patents", ascending=False).head(n)

    def entropy_curve(self, q_range=None):
        if q_range is None:
            q_range = np.linspace(0, 2)
        
        data = self.get_cluster_size_distribution()
        data["Number of inventors"] = data["Number of inventors"] / sum(data["Number of inventors"])

        def hill_number(arr, q):
            if q == 1:
                I = arr > 0
                return np.exp(-np.sum(arr[I] * np.log(arr[I])))
            elif q == 0:
                return np.sum(arr > 0)
            else:
                return np.sum(arr ** (q)) ** (1 / (1 - q))

        return [hill_number(data["Number of inventors"], q) for q in q_range], q_range

    def plot_entropy_curve(self, q_range=None):
        if q_range is None:
            q_range = np.linspace(0, 2)
        
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
                    self._data.groupby("inventor_id")["name_first"]
                    .apply(lambda x: len(set(x)) == 1)
                    .rename("Proportion of unique name")
                )
                .groupby("Number of patents")
                .agg({"Proportion of unique name": "mean"})
                .reset_index()
            )

        return self._cluster_unique_name_distribution.copy()

    def plot_cluster_unique_name_distribution(self, range=(0, 100)):
        """Plot the proportion of homogeneous clusters (no name variation) by cluster size."""
        data = self.get_cluster_unique_name_distribution()
        fig = px.bar(
            data,
            x="Number of patents",
            y="Proportion of unique name",
            title="Proportion of homogeneous clusters (no name variation) by cluster size",
        )
        fig.update_xaxes(range=range)

        ylim = max(data["Proportion of unique name"][data["Number of patents"].between(range[0], range[1])])
        fig.update_yaxes(range=(0, ylim), autorange=False)

        fig.update_traces(name=self.name)
        return fig

    def get_homonymy_rate_distribution(self):
        """Get homonymy rates by cluster size.

        The homonymy rate is the proportion of clusters which share at least one name mention with another cluster.
        """
        if self._homonymy_rate_distribution is None:
            data = self._data.assign(
                inventor_id2=self._data.inventor_id, homophones=self._data.name_first + ":" + self._data.name_last
            )

            dat = (
                data.join(
                    data.groupby("homophones")["inventor_id2"].apply(lambda x: len(set(x)) > 1).rename("Shared name"),
                    on="homophones",
                )[["Shared name", "inventor_id2", "patent_id"]]
                .groupby("inventor_id2")
                .agg({"patent_id": "count", "Shared name": "sum"})
            )

            dat = dat.assign(shared_name_prop=np.where(dat["Shared name"].values > 1, 1, 0))
            result = dat.groupby("patent_id")["shared_name_prop"].agg(np.mean)

            self._homonymy_rate_distribution = result.reset_index().rename(
                columns={"shared_name_prop": "Homonymy rate", "patent_id": "Number of patents"}
            )

        return self._homonymy_rate_distribution.copy()

    def plot_homonymy_rate_distribution(self, range=(0, 100)):
        """Plot homonymy rate by cluster size.

        The homonymy rate is the proportion of clusters which share at least one name mention with another cluster.
        """
        data = self.get_homonymy_rate_distribution().reset_index()
        fig = px.bar(
            data,
            x="Number of patents",
            y="Homonymy rate",
            title="Homonymy rate by cluster size",
        )
        fig.update_xaxes(range=range)

        ylim = max(data["Homonymy rate"][data["Number of patents"].between(range[0], range[1])])
        fig.update_yaxes(range=(0, ylim), autorange=False)

        fig.update_traces(name=self.name)
        return fig
