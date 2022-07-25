try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

data = pd.read_csv("data-raw/harvard-inventors-benchmark/harvard-benchmark-with-reviewed-sequence-number.csv", dtype=str)

data["mention-id"] = "US" + data.patent_number + "-" + data.sequence
data["unique-id"] = data["inventor_id"]

data[["mention-id","unique-id"]].to_csv("pv_evaluation/data/inventor/harvard-inventors-benchmark.csv", index=False)
