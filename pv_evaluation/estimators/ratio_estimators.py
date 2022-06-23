import numpy as np


def ratio_estimator(B, A):
    """Ratio estimator for mean(B)/mean(A) with bias adjustment."""
    assert len(A) == len(B)

    A_mean = np.mean(A)
    B_mean = np.mean(B)
    n = len(A)

    if len(A) == 1:
        adj = 1
    else:
        adj = 1 + ((n - 1) * A_mean) ** (-1) * np.mean(A * (B / B_mean - A / A_mean))

    return adj * B_mean / A_mean


def std_dev(B, A):
    """Standard deviation estimator for ratio estimator."""
    assert len(A) == len(B)

    A_mean = np.mean(A)
    B_mean = np.mean(B)
    n = len(A)

    return (B_mean / A_mean) * np.sqrt(
        np.sum((A / A_mean) ** 2 + (B / B_mean) ** 2 - 2 * (A * B) / (A_mean * B_mean)) / (n * (n - 1))
    )
