try:
    import pandas as pd
except:
    raise Exception("Unable to import pandas. Please install required dependencies.")

pd.read_csv("data-raw/ALS-dataset/als-inventors.csv").to_csv("pv_evaluation/data/inventor/als-inventors.csv", index=False)