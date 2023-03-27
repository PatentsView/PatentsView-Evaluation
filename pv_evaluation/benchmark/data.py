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
        DataFrame: pandas Dataframe with columns "unique_id", "mention_id", "raw_inventor_name_first", and "raw_inventor_name_last".
    """
    with resources.open_text(module, filename) as f:
        data = pd.read_csv(f)

    cols = ["unique_id", "mention_id", "raw_inventor_name_first", "raw_inventor_name_last"]
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
    """
    Loads Lai's 2011 Inventors Benchmark dataset.

    This benchmark dataset is adapted from the dataset reported in Li et al. (2014), which was used to evaluate
    the disambiguation of the U.S. Patent Inventor Database (1975-2010).

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the
    value represents the cluster assignment.

    See:
        Li, G. C., Lai, R., D'Amour, A., Doolin, D. M., Sun, Y., Torvik, V. I., ... & Fleming, L. (2014). Disambiguation and co-authorship networks of the US patent inventor database (1975-2010). Research Policy, 43(6), 941-955.

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.

    Notes:
        * A number of patent IDs which could not be found were removed from Lai's original dataset.
        * Inventor sequence numbers were assigned through automatic matching and manual review. There could be some errors.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "lai-2011-benchmark.csv")


def load_israeli_inventors_benchmark():
    """Loads the Israeli inventors benchmark dataset.

    This benchmark dataset is adapted from Trajenberg and Shiff (2008), which evaluated the U.S. patents granted between 1963 and 1999 for Israeli inventors.

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the
    value represents the cluster assignment.

    See:
        Trajtenberg, M., & Shiff, G. (2008). Identification and mobility of Israeli patenting inventors. Pinhas Sapir Center for Development.

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "israeli-inventors-benchmark.csv")


def load_patentsview_inventors_benchmark():
    """Loads the PatentsView hand-disambiguated inventors benchmark dataset.

    This dataset contains the hand-disambiguation of a set of particularly ambiguous inventor names. The disambiguation process was done manually by experts, to be used as a benchmark for evaluating disambiguation algorithms.

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the
    value represents the cluster assignment.

    See:
        Monath, N., Jones, C., & Madhavan, S. Disambiguating Patent Inventors, Assignees, and their Locations in PatentsView. https://s3.amazonaws.com/data.patentsview.org/documents/PatentsView_Disambiguation_Methods_Documentation.pdf

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "patentsview-inventors-benchmark.csv")


def load_als_inventors_benchmark():
    """
    Loads the Academic Life Sciences inventors benchmark dataset.

    This dataset contains a set of disambiguated inventor mentions derived from Pierre Azoulay's Academic Life Sciences dataset, which covers US patents granted between 1970 and 2005.

    Note that inventor sequence numbers were obtained using a computer matching procedure which may have introduced errors. Rows with unresolved sequence numbers were removed.

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the
    value represents the cluster assignment.

    See:
        Azoulay, P., J. S. Graff Zivin, and G. Manso (2011). Incentives and creativity: evidence from the academic life sciences. The RAND Journal of Economics 42(3), 527-554.

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "als-inventors.csv")


def load_ens_inventors_benchmark():
    """Engineering and Sciences inventors benchmark.

    This is a set of disambiguated inventor mentions derived from Png's LinkedIn-Patent Inventors Dataset for the 2015 PatentsView Disambiguation Workshop.

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the
    value represents the cluster assignment.

    See:
        Ge, Chunmian, Ke-wei Huang, and Ivan P.L. Png, “Engineer/Scientist Careers: Patents, Online Profiles, and Misclassification”, Strategic Management Journal, Vol 37 No 1, January 2016, 232-253.

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "ens-inventors.csv")


def load_binette_2022_inventors_benchmark():
    """
    Loads the Binette's 2022 inventors benchmark dataset.

    The 2022 Binette inventors benchmark is a hand-disambiguated dataset of inventor mentions on granted patents for a sample of inventors from PatentsView.org. The inventors were selected indirectly by sampling inventor mentions uniformly at random, resulting in inventors sampled with probability proportional to their number of granted patents.

    The time period considered is from 1976 to December 31, 2021. This correspond to the disambiguation labeled "disamb_inventor_id_20211230" in PatentsView's bulk data downloads ["g_persistent_inventor.tsv" file](https://patentsview.org/download/data-download-tables)

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.

    References:
        - [Binette, Olivier, Sokhna A York, Emma Hickerson, Youngsoo Baek, Sarvo Madhavan, Christina Jones. (2022). Estimating the Performance of Entity Resolution Algorithms: Lessons Learned Through PatentsView.org. arXiv e-prints: arxiv:2210.01230](https://arxiv.org/abs/2210.01230)

    Notes:
        - The methodology used for the hand-disambiguation is described in the reference.
        - The hand-disambiguation process was done by experts, but it should be expected to contain errors due to the ambiguous nature of inventor disambiguation.
        - The benchmark contains a few extraneous mentions of patents granted outside the considered time period, these should be ignored for evaluation purposes.
        - Given the use of the December 30, 2021, disambiguation from PatentsView as a starting point of the hand-labeling, a bias towards this disambiguation should be expected.
    """
    return load_unique_id_series(INVENTOR_DATA_MODULE, "binette-2022-inventors-benchmark.csv")


def load_air_umass_assignees_benchmark():
    """AIR-UMASS assigness benchmark.

    The dataset is described as follows in the paper referenced below:

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

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.

    References:
        - Monath, N., Jones, C., & Madhavan, S. Disambiguating Patent Inventors, Assignees, and their Locations in PatentsView. https://s3.amazonaws.com/data.patentsview.org/documents/PatentsView_Disambiguation_Methods_Documentation.pdf
    """
    return load_unique_id_series(ASSIGNEE_DATA_MODULE, "air-umass-assignees-benchmark.csv")


def load_nber_subset_assignees_benchmark():
    """AIR-UMASS assigness benchmark.

    The dataset is described as follows in the paper referenced below:

    'The National Bureau of Economic Research provides disambiguated assignee data.
    These data are created semiautomatically with manual correction and labeling of assignee
    coreference decisions produced by string similarity. We grouped the assignee mentions by
    four-letter prefixes and focused on five prefix groups {Moto, Amer, Gene, Solu, Airc} that
    were both common and ambiguous.'

    The dataset is provided in the form of a pandas Series, where the index represents the mention ID and the

    Returns:
        Series: pandas Series with the benchmark data as a membership vector.

    References:
        - Monath, N., Jones, C., & Madhavan, S. Disambiguating Patent Inventors, Assignees, and their Locations in PatentsView. https://s3.amazonaws.com/data.patentsview.org/documents/PatentsView_Disambiguation_Methods_Documentation.pdf
    """
    data = load_unique_id_series(ASSIGNEE_DATA_MODULE, "nber-subset-assignees-benchmark.csv")

    return data[~data.index.duplicated()]
