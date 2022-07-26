try:
    import pandas as pd
    import wget
    import zipfile
    import os
except:
    raise Exception("Unable to import required dependencies.")

if not os.path.isfile("rawinventor.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/rawinventor.tsv.zip")
    with zipfile.ZipFile("rawinventor.tsv.zip", 'r') as zip_ref:
        zip_ref.extractall(".")
    os.remove("rawinventor.tsv.zip")

rawinventor = pd.read_csv("rawinventor.tsv", sep="\t", dtype=str)

data = pd.read_csv("data-raw/harvard-inventors-benchmark/harvard-benchmark-with-reviewed-sequence-number.csv", dtype=str)

data["mention-id"] = "US" + data.patent_number + "-" + data.sequence
data["unique-id"] = data["inventor_id"]

rawinventor["mention-id"] = "US" + rawinventor.patent_id + "-" + rawinventor.sequence
data = data.merge(rawinventor[["mention-id", "name_first", "name_last"]], on="mention-id", how="left")

cols = ["mention-id", "unique-id", "name_first", "name_last"]
data[cols].to_csv("pv_evaluation/data/inventor/harvard-inventors-benchmark.csv", index=False)
