try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

data = pd.read_csv("data-raw/israeli-dataset/uniq_pat.csv")
data["mention-id"] = 'US' + data.patent.astype(str).map(lambda x:x.lstrip('0')) + '-' + (data.invseq - 1).astype(str)
data["unique-id"] = data.id

data[["mention-id", "unique-id", "lastnam", "firstnam", "country"]].to_csv("pv_evaluation/data/inventor/israeli-inventors-benchmark.csv", index=False)