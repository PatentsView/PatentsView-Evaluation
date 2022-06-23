from importlib import resources
import pandas as pd

INVENTOR_DATA_MODULE = "pv_evaluation.data.inventor"


def load_unique_id_series(module, filename):
    """Load disambiguation series from csv file with columns "unique-id" and "mention-id".

    Args:
        module (str): module where file is located.
        filename (str): csv filename.

    Returns:
        Series: pandas Series named "unique-id" and with "mention-id" as an index.
    """
    with resources.open_text(module, filename) as f:
        data = pd.read_csv(f)

    data.set_index("mention-id", inplace=True)
    return data["unique-id"]


def load_lai_2011_inventors_benchmark():
    """Lai's 2011 inventors benchmark dataset (also referred to as as Lai's 2014 inventors benchmark).

    This is adapted from the benchmark dataset reported in Li et al. (2014) to evaluate their disambiguation of the  U.S. Patent Inventor Database (1975-2010).

    Notes:
        * A number of patent IDs which could not be found were removed from Lai's original dataset.
        * Inventor sequence numbers were assigned through automatic matching and manual review. There could be some errors.

    See:
        Li, G. C., Lai, R., D'Amour, A., Doolin, D. M., Sun, Y., Torvik, V. I., ... & Fleming, L. (2014). Disambiguation and co-authorship networks of the US patent inventor database (1975-2010). Research Policy, 43(6), 941-955.

    Returns:
        Series: pandas Series indexed by mention ID and with values corresponding to cluster assignment.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "lai-2011-benchmark.csv")


def load_israeli_inventors_benchmark():
    """Israeli inventors benchmark dataset.

    This is adapted from Trajenberg and Shiff (2008). The data covers U.S. patents granted between 1963 and 1999 for Israeli inventors.

    See:
        Trajtenberg, M., & Shiff, G. (2008). Identification and mobility of Israeli patenting inventors. Pinhas Sapir Center for Development.

    Returns:
        Series: pandas Series indexed by mention ID and with values corresponding to cluster assignment.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "israeli-inventors-benchmark.csv")


def load_patentsview_inventors_benchmark():
    """PatentsView hand-disambiguated inventors benchmark.

    This is the hand-disambiguation of a set of particularly ambiguous inventor names.

    See:
        Monath, N., Jones, C., & Madhavan, S. Disambiguating Patent Inventors, Assignees, and their Locations in PatentsView. https://s3.amazonaws.com/data.patentsview.org/documents/PatentsView_Disambiguation_Methods_Documentation.pdf

    Returns:
        Series: pandas Series indexed by mention ID and with values corresponding to cluster assignment.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "patentsview-inventors-benchmark.csv")
