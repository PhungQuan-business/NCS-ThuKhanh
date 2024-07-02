import os
import pandas as pd
import numpy as np

from typing import List, Dict
import warnings


def find_min_max(a: List):
    min_val = a.min()
    max_val = a.max()
    return min_val, max_val

def create_bin(value):
    if isinstance(value, pd.Series):
        pass
    else:
        try:
            value = pd.Series(value)
            warnings.warn(
                "Input data was not a pandas Series. Converted to pandas Series.", UserWarning)
        except Exception as e:
            raise ValueError(
                f"Input data cannot be converted to a pandas Series: {e}")

    min_val, max_val = find_min_max(value)
    bins = np.linspace(min_val, max_val, 6)
    # bins_round = np.round(bins, 3)
    bin_labels_intervals = [(bins[i], bins[i+1])
                            for i in range(len(bins)-1)]

    value = pd.cut(value, bins=bins,
                   labels=bin_labels_intervals, right=False)

    return value
