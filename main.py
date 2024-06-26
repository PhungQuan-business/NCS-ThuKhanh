import os
import pandas as pd
from src import preprocessing
from utils import _file

TARGET_VALUE = 'is_bad'
data_path = "./data_tbv.xlsx"

if __name__ == "__main__":
    # df = pd.read_excel(data_path, sheet_name=0, nrows=100)
    df = pd.read_excel(data_path)
    
    pp = preprocessing.PreProcessing(df)
    
    # chỗ này phải trả về dataframe
    df_valid = pp.drop_invalid_cols().create_bin()
    
    iv_results = pd.DataFrame(columns=['column', 'IV'])
    iv_results = []
    
    for col in df_valid.columns:
        if col != TARGET_VALUE:
            groupby_table = pp.group_by(df_valid, col_index=df_valid[col], value=TARGET_VALUE)
            pivot_table = pp.make_pivot_table(groupby_table, col, TARGET_VALUE)
            IV = pp.caculcate_IV(pivot_table)
            
            iv_results.append([col, IV])
    iv_results_file = 'IV_results.csv'
    iv_results = pd.DataFrame(iv_results)
    _file.save_IV_to_csv(iv_results, iv_results_file)
    
