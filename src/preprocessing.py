import pandas as pd
import numpy as np
import os
from utils import _data

# TODO move to config
TARGET_VALUE = 'is_bad'


class PreProcessing():
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe
        self.attr_name = dataframe.columns

    def drop_invalid_cols(self):
        # check columns with invalid dtype
        invalid_dtype = _data.get_invalid_attr_dtype(self.dataframe)
        invalid_numeric_attr = _data.get_invalid_numeric_attr(
            self.dataframe)
        print(f'this is length of invalid numeric attr',
              len(invalid_numeric_attr))
        # drop both attributes with wrong data type and invalid numeric attributes
        cols_to_drop = invalid_dtype+invalid_numeric_attr
        print(len(cols_to_drop))
        if TARGET_VALUE in cols_to_drop:
            cols_to_drop.remove(TARGET_VALUE)
        self.dataframe.drop(cols_to_drop, axis=1, inplace=True)

        return self

    def create_bin(self):
        for col in self.dataframe:
            if col != TARGET_VALUE:
                min_val, max_val = _data.find_min_max(self.dataframe[col])
                five_bins = np.linspace(min_val, max_val, 6)
                five_bins_round = np.round(five_bins, 3)
                # assigning label for bins based on calculated interval
                bin_intervals_labels = [(five_bins[i], five_bins[i+1])
                                        for i in range(len(five_bins)-1)]
                # df[col + '_bin'] = pd.cut(df[col], bins=five_bins_round, labels=bin_labels_intervals, right=False)
                self.dataframe[col] = pd.cut(
                    self.dataframe[col], bins=five_bins_round, labels=bin_intervals_labels, right=False)

        return self.dataframe

    def group_by(self, df, col_index, value):
        '''
        col_index: key to group by
        value: value to group by
        '''
        df_group_by = df.groupby(
            [col_index, value], observed=False).size().reset_index(name='count')
        return df_group_by

    def make_pivot_table(self, groupby_table, col_index, value):
        pivoted_df = groupby_table.pivot(
            index=col_index, columns=value, values=groupby_table.columns[-1]).reset_index()
        pivoted_df.columns = [col_index, '0', '1']
        return pivoted_df

    def _woe(self, percent_0, percent_1):
        with np.errstate(divide='ignore', invalid='ignore'):
            return np.where(np.isinf(np.log(percent_0 / percent_1)), 0, np.log(percent_0 / percent_1))

    def caculcate_IV(self, df):
        percentage_0 = np.array(df['0'] / df['0'].sum())
        percentage_1 = np.array(df['1'] / df['1'].sum())

        WOE = self._woe(percentage_0, percentage_1)
        # perform summation even with nan value
        IV = np.nansum((percentage_0 - percentage_1) * WOE)
        return IV
