#! /usr/bin/env python3

import numpy as np
import pandas as pd

from pv_evaluation.metrics import pairwise_precision_recall

reference = pd.read_csv("output/disambiguation.tsv", sep="\t")

ground_truth = []
rates = [5, 10, 20]
for rate in rates:
    np.random.seed(rate)
    prediction = reference.copy()
    k = int(rate * len(prediction) / 100)
    I = np.random.choice(len(prediction), size=k, replace=False)
    J = np.random.choice(len(prediction), size=k)
    prediction.inventor_id[I] = prediction.inventor_id[J]

    prediction.to_csv(f"output/prediction_rate_{rate}.tsv", sep="\t")
    ground_truth.append(
        pairwise_precision_recall(
            prediction.set_index("mention-id")["inventor_id"], reference.set_index("mention-id")["inventor_id"]
        )
    )

pd.DataFrame.from_records(ground_truth, index=rates, columns=["precision", "recall"]).to_csv(
    "output/ground_truth.tsv", sep="\t"
)
