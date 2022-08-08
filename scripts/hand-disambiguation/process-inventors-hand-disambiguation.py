#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="Process inventors hand-disambiguation files: validate data and produce benchmark dataset.")
parser.add_argument("hand_disambiguation", help="Excel spreadsheet with sampled inventor mentions, the corresponding predicted cluster, and lists of inventor mentions to add to and remove from the predicted clusters. This spreadsheet should contain the columns 'patent_id', 'sequence', 'inventor_id', 'add', and 'remove'. The 'add' and 'remove' columns should contain comma-separated inventor mentions in the format US<patent_number>-<sequence_number>.")
parser.add_argument("rawinventor", help="File with reference inventor mentions and predicted clusters. It should contain the columns 'patent_id', 'sequence', and 'inventor_id'.")
parser.add_argument("-o", "--output", help="CSV file where to save the resulting hand-disambiguated membership vector.", default="true_clusters.csv")
parser.add_argument("-d", "--debug", help="Save debugging spreadsheet to '<hand_disambiguation>.csv.debug.xlsx'. This spreadsheet has two pages. The first shows inventor mentions to remove that were not found in the reference predicted clusters. The second shows the name of inventors added to predicted clusters.", action="store_true", default=False)
args = parser.parse_args()

import os
import pandas as pd
import numpy as np

def read_auto(datapath):
    _, ext = os.path.splitext(datapath)

    if ext == ".csv":
        return pd.read_csv(datapath)
    elif ext == ".tsv":
        return pd.read_csv(datapath, sep="\t")
    elif ext in [".parquet", ".pq", ".parq"]:
        return pd.read_parquet(datapath)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(datapath)
    else:
        raise Exception("Unsupported file type. Should be one of csv, tsv, parquet, or xlsx.")

rawinventor = read_auto(args.rawinventor)
rawinventor["mention_id"] = "US" + rawinventor.patent_id.astype(str) + "-" + rawinventor.sequence.astype(str)
disambiguation = rawinventor.set_index("mention_id")["inventor_id"]

def lambd(x):    
    to_add = np.setdiff1d([string.strip() for string in x["add"].split(",")], [""])
    to_remove = np.setdiff1d([string.strip() for string in x["remove"].split(",")], [""])
    cluster = disambiguation[disambiguation == x.inventor_id].index.values
    cluster = np.append(cluster, to_add)
    if len(to_remove) > 0: 
        assert all(mention in cluster for mention in to_remove), f"{to_remove[np.array([mention not in cluster for mention in to_remove])]}"
        cluster =  np.setdiff1d(cluster, to_remove)

    assert all(mention in disambiguation for mention in to_add), f"{to_add[np.array([mention not in disambiguation for mention in to_add])]}"
    
    return cluster

def lambd_remove_errors(x):
    cluster = disambiguation[disambiguation == x.inventor_id].index.values
    to_remove = np.setdiff1d([string.strip() for string in x["remove"].split(",")], [""])
    I = np.array([mention not in cluster for mention in to_remove])
    if len(I > 0):
        return to_remove[I]
    else:
        return []

def lambd_add_errors(x):
    to_add = np.setdiff1d([string.strip() for string in x["add"].split(",")], [""])
    I = np.array([mention not in disambiguation for mention in to_add])
    if len(to_add) > 0:
        return to_add[I]
    else:
        return []

benchmark = read_auto(args.hand_disambiguation).fillna("")
assert all(col in benchmark.columns for col in ["add", "remove", "inventor_id"])

if args.debug:
    with pd.ExcelWriter(f"{args.output}.debug.xlsx") as writer:
        benchmark["remove_errors"] = benchmark.apply(lambd_remove_errors, axis=1)
        benchmark["add_errors"] = benchmark.apply(lambd_add_errors, axis=1)
        benchmark.to_excel(writer, sheet_name="Cluster Errors", index=False)

        benchmark["added"] = benchmark.apply(lambda x : np.setdiff1d([string.strip() for string in x["add"].split(",")], [""]), axis=1)
        dat = benchmark.explode("added")
        dat = dat[~dat.added.isna()]
        dat = dat.merge(rawinventor[["mention_id", "name_first", "name_last"]], left_on="added", right_on="mention_id", suffixes=("", "_added"))
        dat = dat[["patent_id", "sequence", "inventor_id", "name_first", "name_last", "added", "name_first_added", "name_last_added"]]
        dat.to_excel(writer, sheet_name="Validation of Added Mentions", index=False)

else:
    true_clusters = benchmark.apply(lambd, axis=1)
    reference = pd.concat({"inventor_id":benchmark.inventor_id, "mention_id":true_clusters}, axis=1).explode("mention_id").set_index("mention_id")["inventor_id"]
    reference.to_csv(args.output)