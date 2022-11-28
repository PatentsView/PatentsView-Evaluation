try:
    import pandas as pd
    import wget
    import zipfile
    import os
except:
    raise Exception("Unable to import required dependencies.")

if not os.path.isfile("g_inventor_not_disambiguated.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/g_inventor_not_disambiguated.tsv.zip")
    with zipfile.ZipFile("g_inventor_not_disambiguated.tsv.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove("g_inventor_not_disambiguated.tsv.zip")

g_inventor_not_disambiguated = pd.read_csv("g_inventor_not_disambiguated.tsv", sep="\t", dtype=str)

data = pd.read_csv("data-raw/israeli-dataset/uniq_pat.csv", dtype=str)
data["mention_id"] = (
    "US" + data.patent.astype(str).map(lambda x: x.lstrip("0")) + "-" + (data.invseq.astype(int) - 1).astype(str)
)
data["unique_id"] = data.id

g_inventor_not_disambiguated["mention_id"] = (
    "US" + g_inventor_not_disambiguated.patent_id + "-" + g_inventor_not_disambiguated["inventor_sequence"]
)
data = data.merge(
    g_inventor_not_disambiguated[["mention_id", "raw_inventor_name_first", "raw_inventor_name_last"]],
    on="mention_id",
    how="left",
)

cols = ["mention_id", "unique_id", "raw_inventor_name_first", "raw_inventor_name_last"]
data[cols].to_csv("pv_evaluation/data/inventor/israeli-inventors-benchmark.csv", index=False)
