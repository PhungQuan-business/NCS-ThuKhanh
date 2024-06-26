import os
from typing import List
import pandas as pd
import numpy as np

# TODO cái này nhớ chuyển sang config hoặc chỗ nào đó khác
VALID_DTYPE = ['float64', 'int64']
BIN_LENGTH = 5


def find_min_max(a: List):
    """_summary_

    Args:
        a (array_like): input data

    Returns:
        min_value: min value of the input
        max_value: max value of the input
    """
    min_val = a.min()
    max_val = a.max()
    return min_val, max_val


def create_bin(df, col):
    min_val, max_val = find_min_max(df, col)
    five_bins = np.linspace(min_val, max_val, 6)
    five_bins_round = np.round(five_bins, 3)
    bin_labels_intervals = [(five_bins[i], five_bins[i+1])
                            for i in range(len(five_bins)-1)]

    df[col] = pd.cut(df[col], bins=five_bins_round,
                     labels=bin_labels_intervals, right=False)
    return df

# def rename_column(df, old_name, new_name):
#     df = df.rename(columns={old_name: new_name})
#     return df

# Function to append DataFrame to HDF5
# def export_df_to_hdfs(df, file_path, key):
#     if not os.path.isfile(file_path):
#         df.to_hdf(file_path, key, format='table', data_columns=True)
#     else:
#         with pd.HDFStore(file_path) as store:
#             store.append(key, df, format='table', data_columns=True)

# def ensure_consistent_types(df):
#     for col in df.columns:
#         if df[col].dtype == 'object':
#             df[col] = df[col].astype(str)
#     return df

# def add_column(df, col_name, value):
#     df[col_name] = value
#     return df

# def reorder_column(df, col_name):
#     columns = [col_name] + [col for col in df.columns if col != col_name]
#     df = df[columns]
#     return df


def drop_cols(df, cols_to_drop):
    df = df.drop(columns=cols_to_drop)
    return df


def get_invalid_attr_dtype(df):
    # TODO add thêm cái datatype thường dùng
    invalid_cols = [
        col for col in df.columns if df[col].dtype not in ['float64', 'int64']]
    # col = col.dtype in ['float64', 'int64']
    return invalid_cols


def get_invalid_numeric_attr(df):
    # TODO bổ sung đk check nếu có dtype khác thì dừng hoặc làm gì đó(cân nhắc bỏ task)
    invalid_num_cols = [col for col in df.columns if df[col].dtype in VALID_DTYPE and len(
        df[col].unique()) < BIN_LENGTH]
    return invalid_num_cols
