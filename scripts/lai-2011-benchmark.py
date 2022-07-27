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

lai_benchmark = pd.read_csv("data-raw/Lai-2011-data/benchmark_with_sequence.tsv", sep="\t", dtype=str, header=1)

lai_benchmark["mention_id"] = "US" + lai_benchmark.Patent + "-" + lai_benchmark.Sequence
lai_benchmark["unique_id"] = lai_benchmark.UniqueID

rawinventor["mention_id"] = "US" + rawinventor.patent_id + "-" + rawinventor.sequence
lai_benchmark = lai_benchmark.merge(rawinventor[["mention_id", "name_first", "name_last"]], on="mention_id", how="left")

cols = ["mention_id", "unique_id", "name_first", "name_last"]
lai_benchmark[cols].to_csv("pv_evaluation/data/inventor/lai-2011-benchmark.csv", index=False)
