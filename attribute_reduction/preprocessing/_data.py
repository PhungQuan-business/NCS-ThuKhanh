import pandas as pd
import numpy as np
import os
from typing import List, Any, Dict

# TODO move to config
TARGET_VALUE = 'is_bad'

# TODO đổi lại tên


class PreProcessing():
    def __init__(self) -> None:
        pass

    '''
    các chức năng bao gồm:
    -   nghịch đảo cột 
    - 
    '''

    # không khai báo những cái này
    # chỉ khai báo siêu tham số

    def _calculate_reciprocal(self, columns_to_transform: pd.DataFrame):
        columns_to_transform.transform(lambda x: 1 / x)
        return columns_to_transform

    # chỉ cần pass những cột cần thay vì pass toàn bộ dataframe
    def convert_cost_to_benefit(self, columns_to_convert: List):
        converted_columns = self._calculate_reciprocal(columns_to_convert)

        return converted_columns

    # TODO xử lý trường hợp giá trị là nan
    def normalize_attr(self, df):
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                # sum all the value
                sqrt_of_sum = np.sqrt(np.sum(np.square(df[col])))
                print(
                    f'this is sqrt_of_sum of {col}, should be one value', sqrt_of_sum)
                # df.loc[:, col] = df.loc[:, col].astype(np.float32)
                df.loc[:, col] = (df[col] / sqrt_of_sum).astype(np.float32)
        return df

    def cal_attr_weight(self, iv_dict: Dict) -> List:
        iv_values = np.array(iv_dict.values())
        # sum of weight
        sum_IV = np.sum(iv_values)
        attr_weight = iv_values / sum_IV
        # return a list of weight
        return attr_weight

    def keep_attr_with_valid_IV(self, iv_results: Dict[str, float], threshold):
        # keep_columns = []
        # for key, iv_value in iv_results.items():
        #     if iv_value >= threshold:
        #         keep_columns.append(key)

        valid_iv_results = {key: iv_value for key,
                            iv_value in iv_results.items() if iv_value >= threshold}
        return valid_iv_results
