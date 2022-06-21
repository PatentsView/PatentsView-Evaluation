#!/usr/bin/env python3
try:
    import pandas as pd
    import wget
    import zipfile
    import os
except:
    raise Exception("Unable to load required packages. Please check for missing dependencies.")

####################
# rawinventor sample
####################

# Download rawinventor.tsv if not already done.
if not os.path.isfile("rawinventor.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/rawinventor.tsv.zip")
    with zipfile.ZipFile("rawinventor.tsv.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove("rawinventor.tsv.zip")

# Sort rawinventor.tsv by inventor last name and take first 50000 elements.
df = pd.read_csv("rawinventor.tsv", sep="\t")
df.sort_values(by="name_last", inplace=True)
data = df.head(50000)

# Define index and relevant fields
data["mention-id"] = data.patent_id.str.cat(data.sequence.astype(str), sep="-")
data["name_full"] = data.name_first.str.cat(data.name_last, sep="_")

# Save as raw_inventor_sample.tsv
data[["mention-id", "name_full", "inventor_id", "patent_id", "name_first", "name_last"]].to_csv(
    "raw_inventor_sample.tsv", sep="\t", index=False
)
