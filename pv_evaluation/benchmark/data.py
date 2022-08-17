from importlib import resources
import pandas as pd

INVENTOR_DATA_MODULE = "pv_evaluation.data.inventor"
ASSIGNEE_DATA_MODULE = "pv_evaluation.data.assignee"


def load_full_benchmark(module, filename):
    """Load benchmark DataFrame from csv file with columns "unique_id", "mention_id", "name_first", and "name_last".

    Args:
        module (str): module where file is located.
        filename (str): csv filename.

    Returns:
        DataFrame: pandas Dataframe with columns "unique_id", "mention_id", "name_first", and "name_last".
    """
    with resources.open_text(module, filename) as f:
        data = pd.read_csv(f)

    cols = ["unique_id", "mention_id", "name_first", "name_last"]
    return data[cols]


def load_unique_id_series(module, filename):
    """Load disambiguation series from csv file with columns "unique_id" and "mention_id".

    Args:
        module (str): module where file is located.
        filename (str): csv filename.

    Returns:
        Series: pandas Series named "unique_id" and with "mention_id" as an index.
    """
    with resources.open_text(module, filename) as f:
        data = pd.read_csv(f)

    data.set_index("mention_id", inplace=True)
    return data["unique_id"]


def load_lai_2011_inventors_benchmark():
    """Lai's 2011 inventors benchmark dataset (also referred to as as Lai's 2014 inventors benchmark).

    This is adapted from the benchmark dataset reported in Li et al. (2014) to evaluate their disambiguation of the  U.S. Patent Inventor Database (1975-2010).

    See:
        Li, G. C., Lai, R., D'Amour, A., Doolin, D. M., Sun, Y., Torvik, V. I., ... & Fleming, L. (2014). Disambiguation and co-authorship networks of the US patent inventor database (1975-2010). Research Policy, 43(6), 941-955.

    Returns:
        Series: pandas Series indexed by mention ID and with values corresponding to cluster assignment.

    Notes:
        * A number of patent IDs which could not be found were removed from Lai's original dataset.
        * Inventor sequence numbers were assigned through automatic matching and manual review. There could be some errors.
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


def load_als_inventors_benchmark():
    """Academic Life Sciences inventors benchmark.

    This is a set of disambiguated inventor mentions derived from Pierre Azoulay's Academic Life Sciences dataset,
    which covers US patents granted between 1970 and 2005. At this time, no further information is available regarding this dataset.

    Note that inventor sequence numbers were obtained using a computer matching procedure which may have introduced errors.
    Rows with unresolved sequence numbers were removed.

    Returns:
        Series: pandas Series indexed by mention ID and with values corresponding to cluster assignment.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "als-inventors.csv")


def load_ens_inventors_benchmark():
    """Engineering and Sciences inventors benchmark.

    This is a set of disambiguated inventor mentions derived from Png's LinkedIn-Patent Inventors Dataset for the 2015 PatentsView Disambiguation Workshop.
    No further information regarding this dataset is available at this time.

    See:
        Ge, Chunmian, Ke-wei Huang, and Ivan P.L. Png, “Engineer/Scientist Careers: Patents, Online Profiles, and Misclassification”, Strategic Management Journal, Vol 37 No 1, January 2016, 232-253.

    Returns:
        Series: pandas Series indexed by mention ID and with values corresponding to cluster assignment.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "ens-inventors.csv")

def load_air_umass_assignees_benchmark():
    """AIR-UMASS assigness benchmark.

    The dataset is described as follows in [1]:

    'The PatentsView team created a hand-labeled set of disambiguated
    assignee records. The data were created by sampling records of each assignee type
    (universities, federal government entities, private companies, states, and local government
    agencies). We used those records as queries for annotators to find all other records
    referring to the same assignee. Team members annotated the labeled records according to
    string similarity. In cases where an identity could not be confirmed or was uncertain,
    annotators did not create a link. We intended this dataset to have a larger coverage of
    name varieties of the entities than the NBER dataset, which was important for us to
    evaluate the more difficult-to-disambiguate cases. Annotators attempted to label parent
    companies separately from subsidiaries, but the process was more likely to associate
    similarly named child and parent companies than more distinctive ones.'
    
    Returns:
        Series: pandas Series indexed by assignee mention ID and with values corresponding to standardized assignee name.

    References:
        [1] Monath, N., Jones, C., & Madhavan, S. Disambiguating Patent Inventors, Assignees, and their Locations in PatentsView. https://s3.amazonaws.com/data.patentsview.org/documents/PatentsView_Disambiguation_Methods_Documentation.pdf
    """
    return load_unique_id_series(ASSIGNEE_DATA_MODULE, "air-umass-assignees-benchmark.csv")


def load_nber_subset_assignees_benchmark():
    """AIR-UMASS assigness benchmark.

    The dataset is described as follows in [1]:

    'The National Bureau of Economic Research provides disambiguated assignee data.
    These data are created semiautomatically with manual correction and labeling of assignee
    coreference decisions produced by string similarity. We grouped the assignee mentions by
    four-letter prefixes and focused on five prefix groups {Moto, Amer, Gene, Solu, Airc} that
    were both common and ambiguous.'
    
    Returns:
        Series: pandas Series indexed by assignee mention ID and with values corresponding to standardized assignee name.

    References:
        [1] Monath, N., Jones, C., & Madhavan, S. Disambiguating Patent Inventors, Assignees, and their Locations in PatentsView. https://s3.amazonaws.com/data.patentsview.org/documents/PatentsView_Disambiguation_Methods_Documentation.pdf
    """
    return load_unique_id_series(ASSIGNEE_DATA_MODULE, "air-umass-assignees-benchmark.csv")