try:
    import os
    import zipfile

    import pandas as pd
    import wget
except:
    raise Exception("Unable to import required dependencies.")

if not os.path.isfile("g_inventor_not_disambiguated.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/g_inventor_not_disambiguated.tsv.zip")
    with zipfile.ZipFile("g_inventor_not_disambiguated.tsv.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove("g_inventor_not_disambiguated.tsv.zip")

g_inventor_not_disambiguated = pd.read_csv("g_inventor_not_disambiguated.tsv", sep="\t", dtype=str)

lai_benchmark = pd.read_csv("data-raw/Lai-2011-data/benchmark_with_sequence.tsv", sep="\t", dtype=str, header=1)

lai_benchmark["mention_id"] = "US" + lai_benchmark.Patent + "-" + lai_benchmark.Sequence
lai_benchmark["unique_id"] = lai_benchmark.UniqueID

g_inventor_not_disambiguated["mention_id"] = (
    "US" + g_inventor_not_disambiguated.patent_id + "-" + g_inventor_not_disambiguated["inventor_sequence"]
)
lai_benchmark = lai_benchmark.merge(
    g_inventor_not_disambiguated[["mention_id", "raw_inventor_name_first", "raw_inventor_name_last"]],
    on="mention_id",
    how="left",
)

cols = ["mention_id", "unique_id", "raw_inventor_name_first", "raw_inventor_name_last"]
lai_benchmark[cols].to_csv("pv_evaluation/data/inventor/lai-2011-benchmark.csv", index=False)
