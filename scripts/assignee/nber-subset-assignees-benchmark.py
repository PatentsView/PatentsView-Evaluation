try:
    import os
    import zipfile

    import pandas as pd
    import wget
except:
    raise Exception("Unable to import required dependencies.")

if not os.path.isfile("rawassignee.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/rawassignee.tsv.zip")
    with zipfile.ZipFile("rawassignee.tsv.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove("rawassignee.tsv.zip")

rawassignee = pd.read_csv("rawassignee.tsv", sep="\t", dtype=str)

data = pd.read_csv("data-raw/pv-eval-data/assignee/nber-subset/nber-subset.tsv", sep="\t", header=None, dtype=str)
data.columns = ["uuid", "unique_id"]

data = data.merge(rawassignee, on="uuid", how="left")
data["mention_id"] = "US" + data.patent_id + "-" + data.sequence

data = data[["mention_id", "unique_id", "organization"]][~data.mention_id.isna()]

data.to_csv("pv_evaluation/data/assignee/nber-subset-assignees-benchmark.csv", index=False)
