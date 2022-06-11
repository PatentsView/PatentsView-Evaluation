#! /usr/bin/env python3

import pandas as pd
import wget
import zipfile
import os

if not os.path.isfile("output/rawinventor.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/rawinventor.tsv.zip")
    with zipfile.ZipFile("rawinventor.tsv.zip", 'r') as zip_ref:
        zip_ref.extractall(".")
    os.remove("rawinventor.tsv.zip")

rawinventor = pd.read_csv("rawinventor.tsv", sep="\t")
rawinventor["mention-id"] = "US" + rawinventor.patent_id.astype(str) + "-" + rawinventor.sequence.astype(str)
rawinventor[["mention-id", "inventor_id"]].to_csv("output/disambiguation.tsv", sep="\t", index=False)