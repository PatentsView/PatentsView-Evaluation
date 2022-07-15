try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

data = pd.read_csv("data-raw/ALS-dataset/als-inventors.csv")
data.rename(columns={"inventor-id":"unique-id"}, inplace=True)
data = data[~data["mention-id"].duplicated(keep='first')]
data[["mention-id", "unique-id"]].to_csv("pv_evaluation/data/inventor/als-inventors.csv", index=False)