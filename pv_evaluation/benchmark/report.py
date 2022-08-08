import itertools
import pandas as pd
import plotly.express as px

from pv_evaluation.utils import expand_grid

from pv_evaluation.metrics import (
    pairwise_precision,
    pairwise_recall,
    pairwise_fscore,
    cluster_precision,
    cluster_recall,
    cluster_fscore,
    rand_score,
)
from pv_evaluation.benchmark import (
    load_israeli_inventors_benchmark,
    load_patentsview_inventors_benchmark,
    load_lai_2011_inventors_benchmark,
    load_als_inventors_benchmark,
    load_ens_inventors_benchmark,
)
from pv_evaluation.estimators import (
    pairwise_precision_estimator,
    pairwise_precision_std,
    pairwise_recall_estimator,
    pairwise_recall_std,
    cluster_precision_estimator,
    cluster_precision_std,
    cluster_recall_estimator,
    cluster_recall_std,
)

DEFAULT_ESTIMATORS = {
    # Point estimates and standard deviation estimates.
    "pairwise precision": {"point": pairwise_precision_estimator, "std": pairwise_precision_std},
    "pairwise recall": {"point": pairwise_recall_estimator, "std": pairwise_recall_std},
    "cluster precision": {"point": cluster_precision_estimator, "std": cluster_precision_std},
    "cluster recall": {"point": cluster_recall_estimator, "std": cluster_recall_std},
}
INVENTORS_SAMPLES = {
    # Dataset and parameters to pass to the estimator.
    "lai-sample": (load_lai_2011_inventors_benchmark, {"sampling_type": "cluster_block", "weights": "uniform"}),
    "israeli-sample": (load_lai_2011_inventors_benchmark, {"sampling_type": "single_block"}),
}
# Default benchmarks to run.
DEFAULT_INVENTORS_BENCHMARKS = {
    "patentsview-inventors": load_patentsview_inventors_benchmark,
    "israeli-inventors": load_israeli_inventors_benchmark,
    "lai-benchmark": load_lai_2011_inventors_benchmark,
    "als-benchmark": load_als_inventors_benchmark,
    "ens-benchmark": load_ens_inventors_benchmark,
}
DEFAULT_METRICS = {
    "pairwise precision": pairwise_precision,
    "pairwise recall": pairwise_recall,
    # "pairwise f1": pairwise_fscore,
    "cluster precision": cluster_precision,
    "cluster recall": cluster_recall,
    # "cluster f1": cluster_fscore
    # "rand index": rand_score,
}


def inventor_estimates_table(disambiguations, samples, estimators=None):
    """Compute performance estimates for given cluster samples.

    Args:
        disambiguations (dict): dictionary of disambiguation results (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
            Note that the disambiguated population should match the population from which `samples` have been drawn. For instance, if using the Israeli benchmark dataset
            which covers granted patents between granted between 1963 and 1999, then `disambiguations` should be subsetted to the same time period.
        samples (dict): Dictionary of tuples (A, B), where A is a function to load a dataset and B is a dictionary of parameters to pass to estimator functions. See `INVENTORS_SAMPLES` for an example.
        estimators (dict, optional): Dictionary of tuples (A, B) where A is a point estimator and B is a standard deviation estimator. Defaults to DEFAULT_ESTIMATORS.

    Returns:
        DataFrame of estimated performance metrics for every given disambiguation, sample and estimators.
    """
    if estimators is None:
        estimators = DEFAULT_ESTIMATORS

    def compute(sample, estimator, algorithm, type="point"):
        """Compute metric on benchmark data for a given disambiguation algorithm.

        Args:
            benchmark (str): benchmark dataset name.
            metric (str): performance metric name.
            algorithm (str): algorithm name.
            type (str): one of "point" for point estimate or "std" for standard deviation estimate.

        Returns:
            float: Evaluated metric.
        """
        data = pd.concat({"prediction": disambiguations[algorithm], "reference": samples[sample][0]()}, axis=1, join="inner")
        return estimators[estimator][type](data.prediction, data.reference, **samples[sample][1])

    computed_estimates = expand_grid(sample=samples, estimator=estimators, algorithm=disambiguations)
    computed_estimates["value"] = computed_estimates.apply(
        lambda x: compute(x["sample"], x["estimator"], x["algorithm"], type="point"), axis=1
    )
    computed_estimates["std"] = computed_estimates.apply(
        lambda x: compute(x["sample"], x["estimator"], x["algorithm"], type="std"), axis=1
    )
    return computed_estimates


def inventor_estimates_plot(disambiguations, samples, estimators=None, facet_col_wrap=2, **kwargs):
    """Plot performance estimates for given cluster samples.

    Args:
        disambiguations (dict): dictionary of disambiguation results (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
            Note that the disambiguated population should match the population from which `samples` have been drawn. For instance, if using the Israeli benchmark dataset
            which covers granted patents between granted between 1963 and 1999, then `disambiguations` should be subsetted to the same time period.
        samples (dict): Dictionary of tuples (A, B), where A is a function to load a dataset and B is a dictionary of parameters to pass to estimator functions. See `INVENTORS_SAMPLES` for an example.
        estimators (dict, optional): Dictionary of tuples (A, B) where A is a point estimator and B is a standard deviation estimator. Defaults to DEFAULT_ESTIMATORS.

    Returns:
        Plotly bar chart
    """
    if estimators is None:
        estimators = DEFAULT_ESTIMATORS

    computed_metrics = inventor_estimates_table(disambiguations, samples=samples, estimators=estimators)
    return px.bar(
        computed_metrics,
        y="value",
        x="estimator",
        error_y="std",
        color="algorithm",
        facet_col="sample",
        barmode="group",
        facet_col_wrap=facet_col_wrap,
        **kwargs,
    )


def inventor_benchmark_table(disambiguations, metrics=None, benchmarks=None):
    """Compute performance evaluation metrics on benchmark datasets.

    Args:
        disambiguations (dict): dictionary of disambiguation results (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
        metrics (dict, optional): dictionary of metrics (from the metrics submodule) to compute. Defaults to `DEFAULT_METRICS`.
        benchmarks (dict, optional): benchmark datasets loading functions to use from the benchmark submodule. Defaults to `DEFAULT_BENCHMARK`.

    Returns:
        DataFrame of computed metrics for every disambiguations and every benchmark dataset.
    """
    if metrics is None:
        metrics = DEFAULT_METRICS
    if benchmarks is None:
        benchmarks = DEFAULT_INVENTORS_BENCHMARKS

    def compute(benchmark, metric, algorithm):
        """Compute metric on benchmark data for a given disambiguation algorithm.

        Args:
            benchmark (str): benchmark dataset name.
            metric (str): performance metric name.
            algorithm (str): algorithm name.

        Returns:
            float: Evaluated metric.
        """
        data = pd.concat(
            {"prediction": disambiguations[algorithm], "reference": benchmarks[benchmark]()}, axis=1, join="inner"
        )
        return metrics[metric](data.prediction, data.reference)

    computed_metrics = expand_grid(benchmark=benchmarks, metric=metrics, algorithm=disambiguations)

    computed_metrics["value"] = computed_metrics.apply(lambda x: compute(x["benchmark"], x["metric"], x["algorithm"]), axis=1)

    return computed_metrics


def inventor_benchmark_plot(disambiguations, metrics=None, benchmarks=None, facet_col_wrap=2, **kwargs):
    """Bar plot of performance evaluation metrics on benchmark datasets.

    Args:
        disambiguations (dict): dictionary of disambiguation results (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
        metrics (dict, optional): dictionary of metrics (from the metrics submodule) to compute. Defaults to `DEFAULT_METRICS`.
        benchmarks (dict, optional): benchmark datasets loading functions (from the benchmark submodule) to use. Defaults to `DEFAULT_BENCHMARK`.

    Returns:
        plotly graph object
    """
    if metrics is None:
        metrics = DEFAULT_METRICS
    if benchmarks is None:
        benchmarks = DEFAULT_INVENTORS_BENCHMARKS

    computed_metrics = inventor_benchmark_table(disambiguations, metrics=metrics, benchmarks=benchmarks)
    return px.bar(
        computed_metrics,
        y="value",
        x="metric",
        color="algorithm",
        facet_col="benchmark",
        barmode="group",
        facet_col_wrap=facet_col_wrap,
        **kwargs,
    )


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
        disambiguation (Series): disambiguation result Series (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
        benchmark (Series): reference disambiguation Series.
        join_with (DataFrame, optional): DataFrame to join based on "mention_id". Defaults to None.

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
        return clusters_to_split.join(join_with, rsuffix="_joined")
    else:
        return clusters_to_split


def inspect_clusters_to_merge(disambiguation, benchmark, join_with=None):
    """Get table to inspect missing cluster links given a benchmark dataset.

    Args:
        disambiguation (Series): disambiguation result Series (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
        benchmark (Series): reference disambiguation Series.
        join_with (DataFrame, optional): DataFrame to join based on "mention_id". Defaults to None.

    Returns:
        DataFrame: DataFrame containing missing cluster links according to the given benchmark.
    """
    clusters_to_merge = inspect_clusters_to_split(benchmark, disambiguation)
    clusters_to_merge.rename(columns={"prediction": "reference", "reference": "prediction"}, inplace=True)

    if join_with is not None:
        return clusters_to_merge.join(join_with, rsuffix="_joined")
    else:
        return clusters_to_merge
