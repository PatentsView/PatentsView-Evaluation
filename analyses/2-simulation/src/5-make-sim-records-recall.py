#! /usr/bin/env python3

sample_size = [100, 200, 400]

import numpy as np
import pandas as pd
import os
from parse import findall
from pv_evaluation.utils import expand_grid
from pv_evaluation.metrics import pairwise_recall
from pv_evaluation.estimators import pairwise_recall_estimator

rates = [x.named["rate"] for x in findall("prediction_rate_{rate}.tsv", "".join(os.listdir("output/")))]
predictions = {
    rate: pd.read_csv(f"output/prediction_rate_{rate}.tsv", sep="\t").set_index("mention_id")["inventor_id"] for rate in rates
}

reference = pd.read_csv("output/disambiguation.tsv", sep="\t").set_index("mention_id")["inventor_id"]

estimators = {
    "R_naive": lambda ref, benchmark: pairwise_recall(ref, benchmark),
    "R_record": lambda ref, benchmark: pairwise_recall_estimator(ref, benchmark, sampling_type="record", weights="uniform"),
}


def sample_clusters(reference, sample_size):
    clusters = np.random.choice(reference.values, size=sample_size, replace=True)
    return reference[reference.isin(clusters)]


def simulation(estimator, sample_size, rate, repetitions=1):
    estimates = np.zeros(repetitions)
    for i in range(repetitions):
        np.random.seed(i)
        benchmark = sample_clusters(reference, sample_size)
        estimates[i] = estimator(predictions[rate], benchmark)
    return estimates


data = expand_grid(sample_size=sample_size, rate=rates, estimator=estimators.keys())
data["estimates"] = data.apply(
    lambda row: simulation(estimators[row.estimator], row.sample_size, row.rate, repetitions=100), axis=1, result_type="reduce"
)

data.to_pickle("output/estimates_sim_records_recall.pickle")
