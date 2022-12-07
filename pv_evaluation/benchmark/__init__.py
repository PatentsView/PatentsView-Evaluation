"""Evaluation datasets and standardized benchmarks
"""

from pv_evaluation.benchmark.data import (
    load_israeli_inventors_benchmark,
    load_patentsview_inventors_benchmark,
    load_lai_2011_inventors_benchmark,
    load_als_inventors_benchmark,
    load_ens_inventors_benchmark,
    load_binette_2022_inventors_benchmark,
    load_air_umass_assignees_benchmark,
    load_nber_subset_assignees_benchmark,
)

from pv_evaluation.benchmark.report import (
    inventor_estimates_plot,
    inventor_estimates_trend_plot,
    inventor_benchmark_plot,
    inventor_summary_trend_plot,
    inspect_clusters_to_split,
    inspect_clusters_to_merge,
    style_cluster_inspection,
    top_inventors,
    plot_entropy_curves,
    plot_cluster_sizes,
    plot_name_variation_rates,
    plot_homonimy_rates,
)

__all__ = [
    "load_israeli_inventors_benchmark",
    "load_patentsview_inventors_benchmark",
    "load_lai_2011_inventors_benchmark",
    "load_als_inventors_benchmark",
    "load_ens_inventors_benchmark",
    "load_binette_2022_inventors_benchmark",
    "load_harvard_inventors_benchmark",
    "load_air_umass_assignees_benchmark",
    "load_nber_subset_assignees_benchmark",
    "inventor_estimates_plot",
    "inventor_estimates_trend_plot",
    "inventor_benchmark_plot",
    "inventor_summary_trend_plot",
    "inspect_clusters_to_split",
    "inspect_clusters_to_merge",
    "style_cluster_inspection",
    "top_inventors",
    "plot_entropy_curves",
    "plot_cluster_sizes",
    "plot_name_variation_rates",
    "plot_homonimy_rates",
]
