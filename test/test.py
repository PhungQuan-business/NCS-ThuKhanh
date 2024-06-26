import pandas as pd
import numpy as np

cols_1 = ['app_year','req_date', 'ngay_lap_re', 'sex', 'province',
'enc_id', 'enc_phone', 'mstcty', 'mst_encrypt', 'com_business']

cols_2 = ['com_province', 'com_active', 'owner_birthday', 'resi_prov',
'owner_card_issu', 'owner_regi_date', 'habi_prov', 'msisdn',
'quan_huyen', 'tinh_thanh_pho', 'acc_type']


data_path = "./data_tbv.xlsx"


test_data = [['age', 12],
             ['nae', 13]]

if __name__ == "__main__":
    test_df = pd.DataFrame(test_data, columns=['column', 'IV'])
    print(test_df)
    # df = pd.read_excel(data_path, sheet_name=0, nrows=100)
    # print(df.columns[0].dtype)
    
    