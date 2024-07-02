import numpy as np
import pandas as pd
import pprint as pprint
from attribute_reduction.utils._invalid import *
from attribute_reduction.utils._binning import *
from attribute_reduction.utils._file import *
from attribute_reduction.utils._make_table import *
from attribute_reduction.preprocessing._data import PreProcessing

from typing import Dict, List, Any

TARGET_VALUE = 'is_bad'
IV_THRESHHOLD = 0.01


class TopSIS():

    def __init__(self) -> None:
        # khởi tạo các tham số cần cho các method bên dưới
        pass

    def _woe(self, percent_0, percent_1):
        with np.errstate(divide='ignore', invalid='ignore'):
            return np.where(np.isinf(np.log(percent_0 / percent_1)), 0, np.log(percent_0 / percent_1))

    def caculcate_iv(self, pivot_table):
        percentage_0 = np.array(pivot_table['0'] / pivot_table['0'].sum())
        percentage_1 = np.array(pivot_table['1'] / pivot_table['1'].sum())

        WOE = self._woe(percentage_0, percentage_1)
        # perform summation even with nan value
        IV = np.nansum((percentage_0 - percentage_1) * WOE)

        return IV

    def _calculate_weight(self, iv_results: Dict[str, float]):
        iv = np.array(list(iv_results.values()))
        normalized_iv = iv / np.sum(iv)

        normalized_iv_results = {
            key: normalized_iv[i] for i, key in enumerate(iv_results.keys())}

        return normalized_iv_results

    def apply_weight(self, df, iv_results):
        weights = self._calculate_weight(iv_results)
        for col, weight in weights.items():
            if col in df.columns:
                df.loc[:, col] = df[col] * weight

        return df

    def calculate_pis_nis(self, weighted_norm_df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
        PIS = weighted_norm_df.max()
        NIS = weighted_norm_df.min()
        return PIS, NIS

    def calculate_distances(self, weighted_norm_df: pd.DataFrame, PIS: pd.Series, NIS: pd.Series) -> tuple[np.array, np.array]:
        distance_to_pis = np.sqrt(((weighted_norm_df - PIS) ** 2).sum(axis=1))
        distance_to_nis = np.sqrt(((weighted_norm_df - NIS) ** 2).sum(axis=1))
        return distance_to_pis, distance_to_nis

    def cal_similarity(self, distance_to_pis: pd.Series, distance_to_nis: pd.Series):
        similarity_score = distance_to_nis / \
            np.sum([distance_to_nis, distance_to_pis], axis=0)
        return similarity_score

    def rank_alternatives(self, similarity_to_ideal: np.array) -> np.array:
        return np.argsort(similarity_to_ideal)[::-1] + 1

    def fit(self, X, y):
        if isinstance(X, pd.DataFrame):
            pass
        else:
            raise ValueError("the input must be a DataFrame")

        # TODO This is the case where target value is 1d-array
        # there would be case of 2d-array careful
        if isinstance(y, pd.Series):
            pass
        else:
            raise ValueError("the input must be a pandas Series")

        # save all IV result
        self.iv_results = {}

        # TODO quy trình này về sau nhóm vào 1 function hoặc như nào đó
        for col in X.columns:
            # trả về binned pandas Series
            binned_attr = create_bin(X[col])
            groupby_table = group_by(binned_attr, y)
            pivot_table = make_pivot_table(
                groupby_table, X[col], y)
            IV = self.caculcate_iv(pivot_table)

            self.iv_results[col] = IV

        # print(f'this is iv_result before check:', self.iv_results)

        pp = PreProcessing()
        valid_iv_results = pp.keep_attr_with_valid_IV(
            self.iv_results, IV_THRESHHOLD)
        cols_to_keep = valid_iv_results.keys()
        # print(f'this is iv_result after check', valid_iv_results.keys())
        # print(len(valid_iv_results))

        # keep only the valid attributes
        # đến đây là đã lọc ra được các cột thoả mãn đk IV
        X = X[cols_to_keep]
        # print(f'all the retained column', X.columns)
        # ------ Đến đây mới là bắt đầu phase 2---------

        # chuyển các cột cost -> benefit
        # TODO các này đẩy vào init
        cost_attrs = ['tong_tien_t1', 'tong_tien_t3', 'tong_tien_t6']
        # convert trên các cột còn lại sau khi lọc IV
        preserved_cost_attrs = list(set(cost_attrs) & set(X.columns))
        if preserved_cost_attrs is None:
            pass
        else:
            X[preserved_cost_attrs] = pp.convert_cost_to_benefit(
                columns_to_convert=X[preserved_cost_attrs])

        # chuẩn hoá thuộc tính
        X = pp.normalize_attr(X)

        # Nhân attr với weight
        weighted_norm_X = self.apply_weight(X, valid_iv_results)
        # print("weighted_norm_X should contain 1 value", weighted_norm_X)

        PIS, NIS = self.calculate_pis_nis(weighted_norm_X)

        distance_to_pis, distance_to_nis = self.calculate_distances(
            weighted_norm_X, PIS, NIS)
        # print("Distance to PIS:\n", distance_to_pis)
        # print("Distance to NIS:\n", distance_to_nis)

        similarity_score = np.array(self.cal_similarity(distance_to_pis=distance_to_pis,
                                                        distance_to_nis=distance_to_nis))

        ranked_list = self.rank_alternatives(similarity_score)
        return ranked_list
        # print(len(ranked_list))


if __name__ == "__main__":
    data_path = "excel_files/data_tbv.xlsx"
    df = pd.read_excel(data_path)
    # df = pd.read_excel(data_path, sheet_name=0, nrows=100)
    df = drop_invalid_cols(df)
    # print(df['is_bad'])

    topsis = TopSIS()
    X = df.drop([TARGET_VALUE], axis=1)
    y = df[TARGET_VALUE]
    print(type(y))
    topsis.fit(X, y)
