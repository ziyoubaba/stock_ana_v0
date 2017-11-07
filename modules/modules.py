#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np

def read_a_file(filename):
    result = pd.read_csv(filename ,dtype={"code":np.str}, index_col=0 )
    return result

t0 = read_a_file("../data/report_data.csv")
# print(t0)
#

# print(t0[(t0.code=="600602") & (t0.season>=20162)][["code","name","roe","season"]])
data = t0[(t0.code=="600602") & (t0.season>=20162)] #[["roe","season"]]
# print(data)
for index, row in data.iterrows():
    # print(row)
    print(row["code"],int(row["season"]),row["roe"])
    # for i in data.columns:
    #     print(row[i])

t1 = read_a_file("../data/HS_stocks_basic_info.csv")
for _index , a_stock in t1.iterrows():
    print(_index)
    # for i in t1.columns:
    #     print(a_stock[i])
    # print(a_stock["code"])

print(len(t1))