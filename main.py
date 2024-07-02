import numpy as np
import pandas as pd
import pprint as pprint
from attribute_reduction.utils._invalid import *
from attribute_reduction.reduction_model.top_sis import TopSIS

if __name__ == "__main__":
    data_path = "excel_files/data_tbv.xlsx"
    df = pd.read_excel(data_path)
    # df = pd.read_excel(data_path, sheet_name=0, nrows=100)
    df = drop_invalid_cols(df)
    # print(df['is_bad'])

    topsis = TopSIS()
    X = df.drop([TARGET_VALUE], axis=1)
    y = df[TARGET_VALUE]
    
    # cần có 1 function khác để thực hiện ranking, fit thì chỉ là fit thôi
    ranked_list = topsis.fit(X, y)
    print(ranked_list)
    
