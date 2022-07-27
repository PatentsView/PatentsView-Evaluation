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

data = pd.read_csv("data-raw/ALS-dataset/als-inventors.csv", dtype=str)
data.rename(columns={"inventor-id":"unique_id", "mention-id":"mention_id"}, inplace=True)
data = data[~data["mention_id"].duplicated(keep='first')]

rawinventor["mention_id"] = "US" + rawinventor.patent_id + "-" + rawinventor.sequence
data = data.merge(rawinventor[["mention_id", "name_first", "name_last"]], on="mention_id", how="left")

cols = ["mention_id", "unique_id", "name_first", "name_last"]
data[cols].to_csv("pv_evaluation/data/inventor/als-inventors.csv", index=False)
