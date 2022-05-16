import numpy as np
from scipy.special import comb
import pandas as pd



def clusters_count(membership_vect):
    cluster_sizes = np.unique(membership_vect, return_counts=True)[1]
    
    return len(cluster_sizes)

def cluster_precision(prediction, reference):
    
    clusters = pd.DataFrame({"groups": prediction}
                         ).groupby("groups").indices
    
    pass