import os
import pandas as pd
import numpy as np

from typing import List, Dict
import warnings
'''
this helper file responsible for creating table, like pivot table and things like that.
'''


def group_by(value, target_value):
    '''
    col_index: key to group by
    value: value to group by
    '''
    if len(value) != len(target_value):
        raise ValueError(
            "Length of Value to compute and Target value are not the same!")

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

    if isinstance(target_value, pd.Series):
        pass
    else:
        try:
            target_value = pd.Series(target_value)
            warnings.warn(
                "Input data was not a pandas Series. Converted to pandas Series.", UserWarning)
        except Exception as e:
            raise ValueError(
                f"Input data cannot be converted to a pandas Series: {e}")

    # to check if data after conversion remain the same length
    if len(value) != len(target_value):
        raise ValueError(
            "Length of Value to compute and Target value after conversion are not the same!")

    # df = pd.DataFrame([value, target_value], columns=[value.name, target_value.name])
    df = pd.DataFrame({
        value.name: value,
        target_value.name: target_value
    })
    '''
    observed = False để trong trường hợp class '0' = 0,
    bảng kết quả vẫn hiện thị class '0' thay vì bỏ nó đi
    '''
    df_group_by = df.groupby(
        [value.name, target_value.name], observed=False).size().reset_index(name='count')

    return df_group_by


def make_pivot_table(groupby_table, value, target_value):
    pivoted_df = groupby_table.pivot(
        index=value.name, columns=target_value.name, values=groupby_table.columns[-1]).reset_index()
    pivoted_df.columns = [value.name] + \
        pivoted_df.columns[1:].astype(str).tolist()
    return pivoted_df
