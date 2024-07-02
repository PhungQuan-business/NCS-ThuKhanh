import os
from typing import List, Dict
import pandas as pd
import numpy as np

# TODO cái này nhớ chuyển sang config hoặc chỗ nào đó khác
VALID_DTYPE = ['float64', 'int64']
BIN_LENGTH = 5
IV_THRESHHOLD = 0.1
TARGET_VALUE = 'is_bad'


def get_invalid_attr(df) -> List:
    invalid_dtype = [
        col for col in df.columns if not pd.api.types.is_numeric_dtype(df[col])]

    invalid_numeric_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col]) and len(
        df[col].unique()) < BIN_LENGTH]

    return invalid_dtype + invalid_numeric_cols


def drop_invalid_cols(df):
    invalid_attrs = get_invalid_attr(df)
    print(f'this is length of invalid numeric attr',
          len(invalid_attrs))
    # drop both attributes with wrong data type and invalid numeric attributes
    if TARGET_VALUE in invalid_attrs:
        invalid_attrs.remove(TARGET_VALUE)
    df.drop(columns=invalid_attrs, axis=1, inplace=True)

    return df
