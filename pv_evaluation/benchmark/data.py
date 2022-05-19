from importlib import resources
import pandas as pd

INVENTOR_DATA_MODULE = "pv_evaluation.data.inventor"

def load_harvard_inventors_benchmark():
    """TODO: Document this dataset.
    """
    with resources.open_text(INVENTOR_DATA_MODULE, "harvard-inventors-benchmark.csv") as f:
        data = pd.read_csv(f)
    
    data.set_index("mention-id", inplace=True)
    return data["unique-id"]
        
def load_israeli_inventors_benchmark():
    """TODO: Document this dataset.

    Returns:
        _type_: _description_
    """
    with resources.open_text(INVENTOR_DATA_MODULE, "israeli-inventors-benchmark.csv") as f:
        data = pd.read_csv(f)
    
    data.set_index("mention-id", inplace=True)
    return data["unique-id"]

def load_patentsview_inventors_benchmark():
    """TODO: Document dataset.

    Returns:
        _type_: _description_
    """
    with resources.open_text(INVENTOR_DATA_MODULE, "patentsview-inventors-benchmark.csv") as f:
        data = pd.read_csv(f)
    
    data.set_index("mention-id", inplace=True)
    return data["unique-id"]
