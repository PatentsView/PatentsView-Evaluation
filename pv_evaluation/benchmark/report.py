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
    load_harvard_inventors_benchmark,
    load_israeli_inventors_benchmark,
    load_patentsview_inventors_benchmark
)


benchmarks = {
    "patentsview-inventors": load_patentsview_inventors_benchmark,
    "israeli-inventors": load_israeli_inventors_benchmark,
    "harvard-inventors": load_harvard_inventors_benchmark
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


def inspect_clusters_to_split(disambiguation, benchmark):
    data = pd.concat({"prediction":disambiguation, "reference":benchmark}, axis=1, join="inner")
    clusters_to_split = (
        data.join(
            data
            .groupby("prediction")
            .nunique()["reference"]
            .rename("ref_count"), 
        on="prediction")
        .query("ref_count > 1")
        .sort_values("prediction")
        .drop("ref_count", axis=1)    
    )

    return clusters_to_split

def inspect_clusters_to_merge(disambiguation, benchmark):
    table = inspect_clusters_to_split(benchmark, disambiguation)
    
    return table.rename(columns={"prediction":"reference", "reference":"prediction"})
