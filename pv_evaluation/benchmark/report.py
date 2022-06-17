import itertools
import pandas as pd
import plotly.express as px

from pv_evaluation.metrics import (
    pairwise_precision,
    pairwise_recall,
    pairwise_fscore,
    cluster_precision,
    cluster_recall,
    cluster_fscore,
    rand_score,
)
from pv_evaluation.benchmark import load_israeli_inventors_benchmark, load_patentsview_inventors_benchmark

# Default benchmarks to run.
DEFAULT_BENCHMARKS = {
    "patentsview-inventors": load_patentsview_inventors_benchmark,
    "israeli-inventors": load_israeli_inventors_benchmark,
}
DEFAULT_METRICS = {
    "pairwise precision": pairwise_precision,
    "pairwise recall": pairwise_recall,
    # "pairwise f1": pairwise_fscore,
    "cluster precision": cluster_precision,
    "cluster recall": cluster_recall,
    # "cluster f1": cluster_fscore
    "rand index": rand_score,
}


def inventor_benchmark_table(disambiguations, metrics=DEFAULT_METRICS, benchmarks=DEFAULT_BENCHMARKS):
    """Compute performance evaluation metrics on benchmark datasets.

    Args:
        disambiguations (dict): dictionary of disambiguation results (disambiguation results are pandas Series with "mention-id" index and cluster assignment values).
        metrics (dict, optional): Dictionary of metrics (from the metrics submodule) to compute. Defaults to `DEFAULT_METRICS`.
        benchmarks (dict, optional): Benchmark datasets loading functions (from the benchmark submodule) to use. Defaults to `DEFAULT_BENCHMARK`.
    """

    def compute(benchmark, metric, algorithm):
        """Compute metric on benchmark data for a given disambiguation algorithm.

        Args:
            benchmark (str): Benchmark dataset name.
            metric (str): Performance metric name.
            algorithm (str): Algorithm name.

        Returns:
            float: Evaluated metric.
        """
        data = pd.concat(
            {"prediction": disambiguations[algorithm], "reference": benchmarks[benchmark]()}, axis=1, join="inner"
        )
        return metrics[metric](data.prediction, data.reference)

    def expand_grid(data):
        rows = itertools.product(*data.values())
        return pd.DataFrame.from_records(rows, columns=data.keys())

    computed_metrics = expand_grid(dict(benchmark=benchmarks, metric=metrics, algorithm=disambiguations))

    computed_metrics["value"] = computed_metrics.apply(lambda x: compute(x.benchmark, x.metric, x.algorithm), axis=1)

    return computed_metrics


def inventor_benchmark_plot(disambiguations, metrics=DEFAULT_METRICS, benchmarks=DEFAULT_BENCHMARKS, **kwargs):
    """Bar plot of performance evaluation metrics on benchmark datasets.

    Args:
        disambiguations (dict): dictionary of disambiguation results (disambiguation results are pandas Series with "mention-id" index and cluster assignment values).
        metrics (dict, optional): Dictionary of metrics (from the metrics submodule) to compute. Defaults to `DEFAULT_METRICS`.
        benchmarks (dict, optional): Benchmark datasets loading functions (from the benchmark submodule) to use. Defaults to `DEFAULT_BENCHMARK`.

    Returns:
        plotly graph object
    """
    computed_metrics = inventor_benchmark_table(disambiguations, metrics=metrics, benchmarks=benchmarks)
    return px.bar(computed_metrics, y="value", x="metric", color="algorithm", facet_col="benchmark", barmode="group", **kwargs)


def style_cluster_inspection(table, by="prediction"):
    """Style table to highlight groups with alternating colors.

    Args:
        table (dataframe): DataFrame to style.
        by (str, optional): column to color by. Defaults to "prediction".
    """

    def format_color_groups(df):
        # From https://datascientyst.com/pandas-dataframe-background-color-based-condition-value-alternate-row-color-based-group/
        colors = ["white", "#c5dcf5"]
        x = df.copy()
        factors = list(x[by].unique())
        i = 0
        for factor in factors:
            style = f"background-color: {colors[i]}"
            x.loc[x[by] == factor, :] = style
            i = not i
        return x

    return table.style.apply(format_color_groups, axis=None)


def inspect_clusters_to_split(disambiguation, benchmark, join_with=None):
    """Get table of cluster assignment errors on the given benchmark.

    Args:
        disambiguation (Series): Disambiguation result Series.
        benchmark (Series): reference disambiguation Series.
        join_with (DataFrame, optional): DataFrame to join based on "mention-id". Defaults to None.

    Returns:
        DataFrame: DataFrame containing erroneous cluster assignments according to the given benchmark.
    """
    data = pd.concat({"prediction": disambiguation, "reference": benchmark}, axis=1, join="inner")
    clusters_to_split = (
        data.join(data.groupby("prediction").nunique()["reference"].rename("ref_count"), on="prediction")
        .query("ref_count > 1")
        .sort_values("reference")
        .sort_values("prediction")
        .drop("ref_count", axis=1)
    )

    if join_with is not None:
        clusters_to_split = clusters_to_split.join(join_with, rsuffix="_joined")
    else:
        return clusters_to_split


def inspect_clusters_to_merge(disambiguation, benchmark, join_with=None):
    """Get table to inspect missing cluster links given a benchmark dataset.

    Args:
        disambiguation (Series): Disambiguation result Series.
        benchmark (Series): reference disambiguation Series.
        join_with (DataFrame, optional): DataFrame to join based on "mention-id". Defaults to None.

    Returns:
        DataFrame: DataFrame containing missing cluster links according to the given benchmark.
    """
    clusters_to_merge = inspect_clusters_to_split(benchmark, disambiguation)
    clusters_to_merge.rename(columns={"prediction": "reference", "reference": "prediction"}, inplace=True)

    if join_with is not None:
        return clusters_to_merge.join(join_with, rsuffix="_joined")
    else:
        return clusters_to_merge
