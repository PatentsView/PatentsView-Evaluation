import dask.dataframe as dd
import dask.array as da
import pandas as pd
import numpy as np
import os
import tempfile
import shutil
import plotly.express as px


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


class InventorDisambiguationSummary:
    def __init__(self, datapath, processed_data_dir=None):
        """Report inventor disambiguation summaries. Object instanciation is used to manage data pre-processing and speed up some of the computations.

        Args:
            datapath (str): Path to the inventor disambiguation data (csv, tsv or parquet format).
                The data should have four columns: "uuid", "inventor_id", "name_first", and "name_last".
            processed_data_dir (str, optional): Path to a directory where to store processed data.
                Data from past runs will be re-used if it is found in this directory.
                Defaults to None for a temporary directory.
        """
        if processed_data_dir is None:
            processed_data_dir = tempfile.mkdtemp()
            self.tempdir = processed_data_dir
        
        self._parquet_datapath = os.path.join(processed_data_dir, "processed_inventor_disambiguation_data.parquet")
        if os.path.exists(self._parquet_datapath):
            self._data = dd.read_parquet(self._parquet_datapath)
        else:
            self._data = read_auto(datapath)

            # Save indexed data as a parquet file.
            self._data.set_index("inventor_id").to_parquet(self._parquet_datapath)
            self._data = dd.read_parquet(self._parquet_datapath)

        self._validate_data()

        self._cluster_size_distribution = None  # Lazy initialization

    def _validate_data(self):
        for col in ["uuid", "inventor_id", "name_first", "name_last"]:
            assert (col in self._data.columns) or (col in [self._data.index.name]), f"{col} is not in the data columns."

    def __del__(self):
        if hasattr(self, "tempdir"):
            shutil.rmtree(self.tempdir)

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
                .compute()
            )

        return self._cluster_size_distribution

    def get_cluster_sizes_dd(self):
        """Return the number of patents per disambiguated inventor as a Dask DataFrame.

        The mode of the inventor's first name and last name are kept in the resulting dataframe.
        """
        return (
            self._data.groupby("inventor_id")
            .agg({"patent_id": "count", "name_first": "first", "name_last": "first"})
            .rename(columns={"patent_id": "Number of patents"})
        )

    def plot_cluster_size_distribution(self, range=(1, 10)):
        """Plot the distribution of the number of patents per inventor

        Args:
            range (tuple, optional): x-axis limits (inclusive range for the number of patents by inventor). Defaults to (1, 10).

        Returns:
            Plotly graph object.
        """
        data = self.get_cluster_size_distribution().reset_index()
        return px.bar(
            data.iloc[(range[0] - 1) : (range[1]), :],
            x="Number of patents",
            y="Number of inventors",
            title="Distribution of the number of patents per inventor",
        )

    def get_top_inventors(self, n=10):
        """Get DataFrame of n most prolific inventors

        Args:
            n (int, optional): Number of inventors to return. Defaults to 10.

        Returns:
            DataFrame containing the sorted top n most prolific inventors.
        """
        return self.get_cluster_sizes_dd().sort_values(by="Number of patents", ascending=False).head(n)
