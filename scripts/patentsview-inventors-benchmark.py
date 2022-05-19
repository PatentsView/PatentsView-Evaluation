try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

data = pd.read_csv("data-raw/patentsview-inventor/gold-labels.txt", sep="\t", header=None)

mention_numbers = data[0].str.split("-").values

data["mention-id"] = list(map(lambda x: "US"+x[0].lstrip('0')+'-'+x[1], mention_numbers))
data["unique-id"] = data[1]

data[["mention-id", "unique-id"]].to_csv("pv_evaluation/data/inventor/patentsview-inventors-benchmark.csv", index=False)