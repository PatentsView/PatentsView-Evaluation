import numpy as np
import pandas as pd
import os
import plotly.express as px

from pv_evaluation.summary.disambiguation_summary import DisambiguationSummary

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


class InventorDisambiguationSummary(DisambiguationSummary):
    """Report inventor disambiguation summaries."""

    def __init__(self, data, name=None):
        """Constructor.

        Args:
            data (str or DataFrame): pandas DataFrame or string path to the inventor disambiguation data (csv, tsv or parquet format).
                The data should have four columns: "patent_id", "inventor_id", "name_first", and "name_last".
            name (str): name of the disambiguation algorithm to show in plots. Defaults to the provided datapath.
        """
        super().__init__(data, name, "inventor_id")