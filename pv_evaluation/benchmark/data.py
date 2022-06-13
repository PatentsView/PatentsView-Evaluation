from importlib import resources
import pandas as pd

INVENTOR_DATA_MODULE = "pv_evaluation.data.inventor"


def load_unique_id_series(module, filename):
    """Load disambiguation series from csv file with columns "unique-id" and "mention-id".

    Args:
        module (str): module where file is located.
        filename (str): csv filename.

    Returns:
        Series: pandas series named "unique-id" and with "mention-id" as an index.
    """
    with resources.open_text(module, filename) as f:
        data = pd.read_csv(f)

    data.set_index("mention-id", inplace=True)
    return data["unique-id"]


def load_harvard_inventors_benchmark():
    """TODO: Document this dataset.
    """
    # TODO: Fix inventor mention order in this dataset. Right now inventor sequence numbers are mixed up.
    pass
    return load_unique_id_series(INVENTOR_DATA_MODULE, "harvard-inventors-benchmark.csv")

def load_lai_2011_inventors_benchmark():
    """TODO: Document this dataset.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "lai-2011-benchmark.csv")


def load_israeli_inventors_benchmark():
    """TODO: Document this dataset.

    Returns:
        _type_: _description_
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "israeli-inventors-benchmark.csv")


def load_patentsview_inventors_benchmark():
    """TODO: Document dataset.

    Returns:
        _type_: _description_
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "patentsview-inventors-benchmark.csv")
