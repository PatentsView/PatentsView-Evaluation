from .disambiguation_summary import DisambiguationSummary

class InventorDisambiguationSummary(DisambiguationSummary):
    def __init__(self, datapath, name=None):
        """Report inventor disambiguation summaries.

        Args:
            datapath (str): Path to the inventor disambiguation data (csv, tsv or parquet format).
                The data should have four columns: "patent_id", "inventor_id", "name_first", and "name_last".
            name (str): Name of the disambiguation algorithm to show in plots. Defaults to the provided datapath.
        """
        super().__init__(datapath, name=name, id_field="inventor_id")
