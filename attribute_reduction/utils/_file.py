import os
from typing import List, Dict
import pandas as pd
import numpy as np


def save_IV_to_csv(iv_data, filename):

    # Save IV data to CSV file, appending if file exists
    mode = 'a' if os.path.exists(filename) else 'w'
    iv_data.to_csv(filename, mode=mode,
                   header=not os.path.exists(filename), index=False)


def export_to_csv(df, file_path):
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)
