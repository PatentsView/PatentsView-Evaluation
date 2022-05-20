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
)
from pv_evaluation.benchmark import (
    load_israeli_inventors_benchmark,
    load_patentsview_inventors_benchmark
)


benchmarks = {
    "patentsview-inventors": load_patentsview_inventors_benchmark,
    "israeli-inventors": load_israeli_inventors_benchmark,
}
metrics = {
    #"pairwise precision": pairwise_precision,
    #"pairwise recall": pairwise_recall,
    #"pairwise f1": pairwise_fscore,
    "cluster precision": cluster_precision,
    "cluster recall": cluster_recall,
    "cluster f1": cluster_fscore
}


def inventor_benchmark_table(disambiguations, metrics=metrics, benchmarks=benchmarks):
    def compute(benchmark, metric, algorithm):
        data = pd.concat({"prediction":disambiguations[algorithm], "reference":benchmarks[benchmark]()}, axis=1, join="inner")
        return metrics[metric](data.prediction, data.reference)

    def expand_grid(data):
        rows = itertools.product(*data.values())
        return pd.DataFrame.from_records(rows, columns=data.keys())

    computed_metrics = expand_grid(dict(
        benchmark = benchmarks,
        metric = metrics,
        algorithm = disambiguations
    ))


    computed_metrics["value"] = computed_metrics.apply(lambda x: compute(x.benchmark, x.metric, x.algorithm), axis=1)

    return computed_metrics


def inventor_benchmark_plot(disambiguations, **kwargs):
    computed_metrics = inventor_benchmark_table(disambiguations)
    return px.bar(computed_metrics, y="value", x="metric", color="algorithm", facet_col="benchmark", barmode='group', **kwargs)

def style_cluster_inspection(table):
    def format_color_groups(df):
        # From https://datascientyst.com/pandas-dataframe-background-color-based-condition-value-alternate-row-color-based-group/
        colors = ['white', 'lightblue']
        x = df.copy()
        factors = list(x['prediction'].unique())
        i = 0
        for factor in factors:
            style = f'background-color: {colors[i]}'
            x.loc[x['prediction'] == factor, :] = style
            i = not i
        return x
        
    return table.style.apply(format_color_groups, axis=None)

def inspect_clusters_to_split(disambiguation, benchmark, join_with=None):
    data = pd.concat({"prediction":disambiguation, "reference":benchmark}, axis=1, join="inner")
    clusters_to_split = (
        data.join(
            data
            .groupby("prediction")
            .nunique()["reference"]
            .rename("ref_count"), 
        on="prediction")
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
    clusters_to_merge = inspect_clusters_to_split(benchmark, disambiguation)
    clusters_to_merge.rename(columns={"prediction":"reference", "reference":"prediction"}, inplace=True)
    
    if join_with is not None:
        return clusters_to_merge.join(join_with, rsuffix="_joined")
    else:
        return clusters_to_merge
