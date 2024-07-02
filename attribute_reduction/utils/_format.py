import os
from typing import List, Dict
import pandas as pd
import numpy as np


def list_to_dict(lst):
    if not all(len(sublist) == 2 for sublist in lst):
        raise ValueError("All sub-lists must contain exactly two elements.")
    return dict(lst)


def dict_to_list(d):
    return [[key, value] for key, value in d.items()]
