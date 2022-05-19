try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

data = pd.read_csv("data-raw/harvard-inventors-benchmark/combined_labels_HarvardInv.txt", sep="|")

data["ManualIDs"] = data.ManualIDs.str.split(",")
data["name"] = data.RawNames.str.split(",")
data["invseq"] = data.ManualIDs.apply(lambda x: range(len(x)))
data = data.explode(["ManualIDs", "name", "invseq"])

data["mention-id"] = data.Pub_number + "-" + data.invseq.astype(str)
data["unique-id"] = data["ManualIDs"]

data[["mention-id","unique-id","name"]].to_csv("pv_evaluation/data/inventor/harvard-inventors-benchmark.csv", index=False)