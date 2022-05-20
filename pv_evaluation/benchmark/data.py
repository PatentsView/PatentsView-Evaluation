from importlib import resources
import pandas as pd

INVENTOR_DATA_MODULE = "pv_evaluation.data.inventor"

def load_unique_id_series(module, filename):
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
