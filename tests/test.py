import pandas as pd
import numpy as np
from attribute_reduction.preprocessing._data import PreProcessing

# from ..src.preprocessing import PreProcessing
# cols_1 = ['app_year','req_date', 'ngay_lap_re', 'sex', 'province',
# 'enc_id', 'enc_phone', 'mstcty', 'mst_encrypt', 'com_business']

# cols_2 = ['com_province', 'com_active', 'owner_birthday', 'resi_prov',
# 'owner_card_issu', 'owner_regi_date', 'habi_prov', 'msisdn',
# 'quan_huyen', 'tinh_thanh_pho', 'acc_type']


# test_data = [['age', 12],
#              ['nae', 13]]
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
# Example usage


if __name__ == "__main__":
    
    arr1 = [1,2,3,4]
    arr2 = [5,6,7,8]
    sum_arr = np.sum([arr1, arr2], axis=0)
    print(sum_arr)
    result = arr2 / sum_arr
    print(result)
    data_path = "excel_files/data_tbv.xlsx"
    # # test_df = pd.DataFrame(test_data, columns=['column', 'IV'])
    df = pd.read_excel(data_path, sheet_name=0, nrows=100)
    
    pp = PreProcessing()

    # # print(pd.api.types.is_numeric_dtype)
    # # print(f'before transform', df[col])
    # # df[col] = 1/df[col]
    # # print(f'after transform', df[col])

    # col = ['tong_tien_t6', 'tong_tien_t3']
    # # iv_dict = {'A': 0.05, 'B': 0.2, 'C': 0.08, 'D': 0.15}
    # print(df[col])
    # df = pp.calculate_reciprocal(df, col)
    # print(df[col])
    # result = iv_list.get_first_sublist()
    # print(result)
