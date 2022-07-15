try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

data = pd.read_csv("data-raw/patentsview-2015-workshop-datasets/eval/eval_ens.txt", sep="\t", header=None)
data.columns = ["mention-id", "unique-id"]
data["mention-id"] = "US" + data["mention-id"]
data.to_csv("pv_evaluation/data/inventor/ens-inventors.csv", index=False)