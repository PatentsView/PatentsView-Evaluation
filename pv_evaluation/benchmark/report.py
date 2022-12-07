import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime


from er_evaluation.utils import expand_grid
from er_evaluation.estimators import estimates_table, pairwise_precision_design_estimate, pairwise_recall_design_estimate
from er_evaluation.summary import (
    cluster_sizes,
    name_variation_rate,
    homonimy_rate,
    matching_rate
)
from er_evaluation.metrics import (
    metrics_table,
    pairwise_precision,
    pairwise_recall,
)
from er_evaluation.plots import (
    compare_plots,
    plot_entropy_curve,
    plot_cluster_sizes_distribution,
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
    "binette-sample": {
        "sample": load_binette_2022_inventors_benchmark(),
        "weights": 1 / cluster_sizes(load_binette_2022_inventors_benchmark()),
    },
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


def inventor_summary_trend_plot(persistent_inventor, names):
    """Plot key performance metrics over time.

    Args:
        persisten_inventor (DataFrame): String-valued DataFrame in the format of PatentsView's bulk data download file "g_persistent_inventor.tsv". This should contain the columns "patent_id", "sequence", as well as columns with names of the form "disamb_inventor_id_YYYYMMDD" for inventor IDs corresponding to the given disambiguation date.
        names (Series): pandas Series indexed by mention IDs and with values corresponding to mentioned inventor name.

    Returns:
        Plotly scatter plot of the matching rate, homonymy rate, and name variation rate.
    """
    persistent_inventor["mention_id"] = "US" + persistent_inventor.patent_id + "-" + persistent_inventor.sequence
    persistent_inventor.set_index("mention_id", inplace=True)

    disambiguation_names = [s for s in persistent_inventor.columns.values if s.startswith("disamb")]
    disambiguations = {s.lstrip("disamb_inventor_id_"):persistent_inventor[s].dropna() for s in disambiguation_names}

    metrics = {
        "Matching rate": lambda x: matching_rate(x),
        "Homonimy rate": lambda x: homonimy_rate(x, names),
        "Name variation rate": lambda x: name_variation_rate(x, names),
    }

    data = expand_grid(disambiguation=disambiguations, metric=metrics)
    data["value"] = data.apply(lambda x: metrics[x.metric](disambiguations[x.disambiguation]), axis=1)

    data["date"] = data["date"] = pd.to_datetime([datetime.strptime(d, "%Y%m%d") for d in data["disambiguation"]])

    fig = px.line(
        data,
        y="value",
        x="date",
        color="metric",
        symbol="metric",
        color_discrete_sequence=px.colors.qualitative.Vivid,
    )
    fig.update_layout(yaxis_range=(0,1))

    return fig


def inventor_estimates_trend_plot(persistent_inventor, samples_weights=None, estimators=None, **kwargs):
    """Plot performance estimates over time.

    Note:
        The timeframe for the disambiguation should match the timeframe considered by the reference sample.

    Args:
        persisten_inventor (DataFrame): String-valued DataFrame in the format of PatentsView's bulk data download file "g_persistent_inventor.tsv". This should contain the columns "patent_id", "sequence", as well as columns with names of the form "disamb_inventor_id_YYYYMMDD" for inventor IDs corresponding to the given disambiguation date.
        samples (dict): Dictionary of tuples (A, B), where A is a function to load a dataset and B is a dictionary of parameters to pass to estimator functions. See `INVENTORS_SAMPLES` for an example.
        estimators (dict, optional): Dictionary of tuples (A, B) where A is a point estimator and B is a standard deviation estimator. Defaults to DEFAULT_ESTIMATORS.

    Returns:
        Plotly scatter plot
    """
    if estimators is None:
        estimators = DEFAULT_ESTIMATORS
    if samples_weights is None:
        samples_weights = DEFAULT_INVENTORS_SAMPLES_WEIGHTS

    persistent_inventor["mention_id"] = "US" +persistent_inventor.patent_id + "-" + persistent_inventor.sequence
    persistent_inventor.set_index("mention_id", inplace=True)

    disambiguation_names = [s for s in persistent_inventor.columns.values if s.startswith("disamb")]
    disambiguations = {s.lstrip("disamb_inventor_id_"):persistent_inventor[s].dropna() for s in disambiguation_names}

    computed_metrics = estimates_table(disambiguations, samples_weights=samples_weights, estimators=estimators)
    computed_metrics["date"] = pd.to_datetime([datetime.strptime(d, "%Y%m%d") for d in computed_metrics["prediction"]])

    return px.line(
        computed_metrics,
        y="value",
        x="date",
        error_y="std",
        color="estimator",
        symbol="estimator",
        color_discrete_sequence=px.colors.qualitative.Vivid,
    )


def inventor_estimates_plot(disambiguations, samples_weights=None, estimators=None, facet_col_wrap=2, **kwargs):
    """Plot performance estimates for given cluster samples.

    Note:
        The timeframe for the disambiguation should match the timeframe considered by the reference sample.

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
        color="prediction",
        facet_col="sample_weights",
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
        color="prediction",
        facet_col="reference",
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


def top_inventors(disambiguation, names, n=10):
    """
    Table of most prolific inventors

    Args:
        disambiguation (Series): Membership vector, indexed by mention IDs, representing a given disambiguation.
        names (Series): Pandas Series indexed by mention IDs and with values corresponding to inventor name.
        n (int, optional): Number of rows to display. Defaults to 10.

    Returns:
        DataFrame: Table with top n most prolific inventors.
    """
    largest = cluster_sizes(disambiguation).sort_values(ascending=False).head(n)
    largest_mentions = disambiguation[np.isin(disambiguation.values, largest.index.values)]
    largest_with_names = pd.merge(largest_mentions, names, how="left", left_index=True, right_index=True)

    return largest_with_names.groupby(disambiguation.name).first()


def plot_entropy_curves(disambiguations):
    """
    Plot entropy curves for a set of disambiguations

    Args:
        disambiguations (Dict): Dictionary of membership vectors representing given disambiguations

    Returns:
        Plotly figure.
    """
    fig = compare_plots(*[plot_entropy_curve(d, name=k) for k, d in disambiguations.items()])
    fig.update_layout(
        autosize=False, width=800, title="Hill numbers Curve", xaxis_title="q", yaxis_title="Hill number of order q"
    )
    fig.update_yaxes(autorange=True)
    return fig


def plot_cluster_sizes(disambiguations):
    """
    Plot cluster sizes for a set of disambiguations

    Args:
        disambiguations (Dict): Dictionary of membership vectors representing given disambiguations.

    Returns:
        Plotly figure.
    """
    fig = compare_plots(*[plot_cluster_sizes_distribution(d, name=k, normalize=True) for k, d in disambiguations.items()])
    fig.update_layout(
        autosize=False, width=800, title="Cluster Sizes Distribution", xaxis_title="Cluster size", yaxis_title="Proportion"
    )
    fig.update_xaxes(range=(0, 20))
    fig.update_yaxes(autorange=True)
    return fig


def plot_name_variation_rates(disambiguations, names):
    """
    Plot name variation rates for a set of given disambiguations

    Args:
        disambiguations (Dict): Dictionary of membership vectors representing given disambiguations.
        names (Series): Pandas Series indexed by mention IDs and with values corresponding to inventor name.

    Returns:
        Plotly figure.
    """
    rates = [name_variation_rate(disambiguations[f], names=names) for f in disambiguations.keys()]

    data = pd.DataFrame({"Name variation rate": rates, "Disambiguation": disambiguations.keys(), "none": ""})

    fig = px.bar(data, x="none", y="Name variation rate", color="Disambiguation", barmode="group")
    fig.update_layout(title="Name variation rate", xaxis_title="")
    fig.update_yaxes(range=(0, 1))
    return fig


def plot_homonimy_rates(disambiguations, names):
    """
    Plot homonimy rates for a set of given disambiguations

    Args:
        disambiguations (Dict): Dictionary of membership vectors representing given disambiguations.
        names (Series): Pandas Series indexed by mention IDs and with values corresponding to inventor name.

    Returns:
        Plotly figure.
    """

    rates = [homonimy_rate(disambiguations[f], names=names) for f in disambiguations.keys()]
    data = pd.DataFrame({"Homonimy rate": rates, "Disambiguation": disambiguations.keys(), "none": ""})

    fig = px.bar(data, x="none", y="Homonimy rate", color="Disambiguation", barmode="group")
    fig.update_layout(title="Homonimy rate", xaxis_title="")
    fig.update_yaxes(range=(0, 1))
    return fig
