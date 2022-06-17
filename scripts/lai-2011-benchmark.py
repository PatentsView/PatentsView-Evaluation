try:
    import pandas as pd
except:
    raise Exception("Unable to import required dependencies.")

lai_benchmark = pd.read_csv("data-raw/Lai-2011-data/benchmark_with_sequence.tsv", sep="\t", dtype=str, header=1)

lai_benchmark["mention-id"] = "US" + lai_benchmark.Patent + "-" + lai_benchmark.Sequence
lai_benchmark["unique-id"] = lai_benchmark.UniqueID
lai_benchmark[["mention-id", "unique-id"]].to_csv("pv_evaluation/data/inventor/lai-2011-benchmark.csv", index=False)
