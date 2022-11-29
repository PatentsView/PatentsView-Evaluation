import itertools
import pandas as pd
import plotly.express as px

from er_evaluation.utils import expand_grid
from er_evaluation.estimators import (
    estimates_table,
    pairwise_precision_design_estimate,
    pairwise_recall_design_estimate
)
from er_evaluation.summary import (
    cluster_sizes
)
from er_evaluation.metrics import (
    metrics_table,
    pairwise_precision,
    pairwise_recall,
)

from pv_evaluation.benchmark import (
    load_israeli_inventors_benchmark,
    load_patentsview_inventors_benchmark,
    load_lai_2011_inventors_benchmark,
    load_als_inventors_benchmark,
    load_ens_inventors_benchmark,
    load_binette_2022_inventors_benchmark,
)

DEFAULT_ESTIMATORS = {
    # Point estimates and standard deviation estimates.
    "pairwise precision": pairwise_precision_design_estimate,
    "pairwise recall": pairwise_recall_design_estimate,
}
DEFAULT_INVENTORS_SAMPLES_WEIGHTS = {
    # Dataset and parameters to pass to the estimator.
    "lai-sample": {"sample":load_lai_2011_inventors_benchmark(), "weights":1/cluster_sizes(load_lai_2011_inventors_benchmark())},
    "binette-sample": {"sample":load_binette_2022_inventors_benchmark(), "weights":1/cluster_sizes(load_binette_2022_inventors_benchmark())},
}
# Default benchmarks to run.
DEFAULT_INVENTORS_BENCHMARKS = {
    "patentsview-inventors": load_patentsview_inventors_benchmark(),
    "israeli-inventors": load_israeli_inventors_benchmark(),
    "lai-benchmark": load_lai_2011_inventors_benchmark(),
    "als-benchmark": load_als_inventors_benchmark(),
    "ens-benchmark": load_ens_inventors_benchmark(),
    "binette-benchmark": load_binette_2022_inventors_benchmark(),
}
DEFAULT_METRICS = {
    "pairwise precision": pairwise_precision,
    "pairwise recall": pairwise_recall,
}

def inventor_estimates_plot(disambiguations, samples_weights, estimators=None, facet_col_wrap=2, **kwargs):
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
    if samples_weights is None:
        samples_weights = DEFAULT_INVENTORS_SAMPLES_WEIGHTS

    computed_metrics = estimates_table(disambiguations, samples_weights=samples_weights, estimators=estimators)
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


def inventor_benchmark_plot(predictions, references=None, metrics=None, facet_col_wrap=2, **kwargs):
    """Bar plot of performance evaluation metrics on benchmark datasets.

    Args:
        disambiguations (dict): dictionary of disambiguation results (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
        metrics (dict, optional): dictionary of metrics (from the metrics submodule) to compute. Defaults to `DEFAULT_METRICS`.
        benchmarks (dict, optional): benchmark datasets loading functions (from the benchmark submodule) to use. Defaults to `DEFAULT_BENCHMARK`.

    Returns:
        plotly graph object
    """
    if references is None:
        references = DEFAULT_INVENTORS_BENCHMARKS
    if metrics is None:
        metrics = DEFAULT_METRICS

    computed_metrics = metrics_table(predictions, references, metrics)
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


def add_links(table, type="patentsview"):
    """Add Google Patents links to table with mention IDs as index.

    Args:
        table (DataFrame): pandas DataFrame with mention IDs as an index.

    Returns:
        DataFrame: table with added Google Patents links.
    """

    if len(table) > 0:
        patent_codes = table.index.str.split("-", expand=True).droplevel(1).str.lstrip("US").values
        table["link"] = [
            f"<a class='previewbox-anchor' href='https://datatool.patentsview.org/#detail/patent/{x}'>🔗</a>"
            for x in patent_codes
        ]
    return table


def inspect_clusters_to_split(disambiguation, benchmark, join_with=None, links=False):
    """Get table of cluster assignment errors on the given benchmark.

    Args:
        disambiguation (Series): disambiguation result Series (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
        benchmark (Series): reference disambiguation Series.
        join_with (DataFrame, optional): DataFrame indexed by "mention_id". Defaults to None.

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
        table = clusters_to_split.join(join_with, rsuffix="_joined")
    else:
        table = clusters_to_split

    if links:
        table = add_links(table)

    return table


def inspect_clusters_to_merge(disambiguation, benchmark, join_with=None, links=False):
    """Get table to inspect missing cluster links given a benchmark dataset.

    Args:
        disambiguation (Series): disambiguation result Series (disambiguation results are pandas Series with "mention_id" index and cluster assignment values).
        benchmark (Series): reference disambiguation Series.
        join_with (DataFrame, optional): DataFrame indexed by "mention_id". Defaults to None.

    Returns:
        DataFrame: DataFrame containing missing cluster links according to the given benchmark.
    """
    clusters_to_merge = inspect_clusters_to_split(benchmark, disambiguation)
    clusters_to_merge.rename(columns={"prediction": "reference", "reference": "prediction"}, inplace=True)

    if join_with is not None:
        table = clusters_to_merge.join(join_with, rsuffix="_joined")
    else:
        table = clusters_to_merge

    if links:
        table = add_links(table)

    return table
