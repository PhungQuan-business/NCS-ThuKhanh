import pandas as pd
import numpy as np
from attribute_reduction.utils._invalid import *
from attribute_reduction.utils._binning import *
from attribute_reduction.utils._file import *
from attribute_reduction.utils._make_table import *
from attribute_reduction.reduction_model.top_sis import TopSIS
from attribute_reduction.preprocessing._data import PreProcessing


class PP():

    def __init__(self) -> None:
        pass

    def list_to_dict(lst):
        """
        Converts a list of lists to a dictionary.

        Parameters:
        lst (list): List of lists, where each sub-list contains two elements [key, value].

        Returns:
        dict: Dictionary with keys and values from the input list of lists.
        """
        if not all(len(sublist) == 2 for sublist in lst):
            raise ValueError(
                "All sub-lists must contain exactly two elements.")
        return dict(lst)

    def dict_to_list(self, d):
        """
        Converts a dictionary to a list of lists.

        Parameters:
        d (dict): Dictionary to be converted.

        Returns:
        list: List of lists, where each sub-list contains two elements [key, value].
        """
        self.data = [[key, value] for key, value in d.items()]
        return self

    def get_first_sublist(self):
        result = self.data[0]
        return result


if __name__ == "__main__":
    data_path = "excel_files/data_tbv.xlsx"
    df = pd.read_excel(data_path)
    # df = pd.read_excel(data_path, sheet_name=0, nrows=100)
    power_2 = np.square(df.age)
    print(np.sqrt(sum(power_2)))
    # pp = PreProcessing()
    # cost_attrs = ['tong_tien_t1', 'tong_tien_t3', 'tong_tien_ttt']
    # preserved_cost_attrs = list(set(cost_attrs) & set(df.columns))
    # df[preserved_cost_attrs] = pp.convert_cost_to_benefit(
    #     columns_to_convert=df[preserved_cost_attrs])
    # print(df[preserved_cost_attrs])
    # print(df.head())
    # x = df['age']
    # y = df['is_bad']

    # x = create_bin(x)
    # print(f'this is x:', x)
    # groupby_table = group_by(x, y)
    # print(f'this is group by table', groupby_table)
    # pivot_table = make_pivot_table(groupby_table, x, y)

    # print(f'this is pivot table', pivot_table)
    # topsis = TopSIS()
    # IV = topsis.caculcate_IV(pivot_table)
    # print(f'this is IV:I', IV)
