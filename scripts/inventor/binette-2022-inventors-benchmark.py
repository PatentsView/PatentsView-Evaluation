try:
    import os
    import subprocess
    import zipfile

    import pandas as pd
    import wget
except:
    raise Exception("Unable to import required dependencies.")

if not os.path.isfile("g_inventor_not_disambiguated.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/g_inventor_not_disambiguated.tsv.zip")
    with zipfile.ZipFile("g_inventor_not_disambiguated.tsv.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove("g_inventor_not_disambiguated.tsv.zip")

if not os.path.isfile("g_persistent_inventor.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/g_persistent_inventor.tsv.zip")
    with zipfile.ZipFile("g_persistent_inventor.tsv.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove("g_persistent_inventor.tsv.zip")

subprocess.run(
    [
        "process-inventors-hand-disambiguation.py",
        "data-raw/Binette-2022-inventors-benchmark/Binette-2022-inventors-benchmark-hand-labeling.xlsx",
        "g_inventor_not_disambiguated.tsv",
        "g_persistent_inventor.tsv",
        "disamb_inventor_id_20211230",
        "-o",
        "pv_evaluation/data/inventor/binette-2022-inventors-benchmark.csv",
    ]
)
