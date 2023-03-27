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

data = pd.read_csv("data-raw/patentsview-inventor/gold-labels.txt", sep="\t", header=None, dtype=str)

mention_numbers = data[0].str.split("-").values

data["mention_id"] = list(map(lambda x: "US" + x[0].lstrip("0") + "-" + x[1], mention_numbers))
data["unique_id"] = data[1]

g_inventor_not_disambiguated["mention_id"] = (
    "US" + g_inventor_not_disambiguated.patent_id + "-" + g_inventor_not_disambiguated["inventor_sequence"]
)
data = data.merge(
    g_inventor_not_disambiguated[["mention_id", "raw_inventor_name_first", "raw_inventor_name_last"]],
    on="mention_id",
    how="left",
)

cols = ["mention_id", "unique_id", "raw_inventor_name_first", "raw_inventor_name_last"]
data[cols].to_csv("pv_evaluation/data/inventor/patentsview-inventors-benchmark.csv", index=False)
