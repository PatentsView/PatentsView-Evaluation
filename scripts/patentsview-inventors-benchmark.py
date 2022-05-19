try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

data = pd.read_csv("data-raw/patentsview-inventor/gold-labels.txt", sep="\t", header=None)

data["mention-id"] = "US" + data[0]
data["unique-id"] = data[1]

data[["mention-id", "unique-id"]].to_csv("pv_evaluation/data/inventor/patentsview-inventors-benchmark.csv", index=False)