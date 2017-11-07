#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import tushare as ts

# 2 get season report
def season_report(year,which_season,tocsv=True):
    """
    :param year: year
    :param which_season: 1/2/3/4
    :return:
    """
    print("\ndownld : {0}/{1}".format(year, which_season))
    report_data = pd.DataFrame()
    try:
        report_data = ts.get_report_data(year,which_season)
    except OSError as e:
        print(e)
        # print("\n")
    except Exception as e:
        print(e)
        # print("\n")
    if tocsv and not report_data.empty:
        report_data.to_csv("./data/report_data/report_data_{0}_{1}.csv".format(year,which_season))
    return report_data

# download season_report of many years
def season_report_downloader():
    for a_year in range(2017,2018):
        for season in range(1,5):
            season_report(a_year , season)

import os
# 合并各个季度的报表到一个文件里
class Unioner():
    def __init__(self):
        self.dictionary = "./data/report_data/"

    def list_csv_files(self):
        files = os.walk(self.dictionary)
        for dir_name , sub_dir_name , csv_files in files:
            if not sub_dir_name:
                csv_files.sort()
                for a_csv in csv_files:
                    if a_csv.startswith("report_data_"):
                        yield os.path.join(dir_name,a_csv)

    def union(self):
        data_list = []
        for a_file in self.list_csv_files():
            season_str = a_file.split("report_data_")[-1].split(".")[0].replace("_","")
            csv_data = pd.read_csv(a_file,dtype={"code":np.str},index_col=0)
            csv_data = csv_data.drop_duplicates()   # 去重
            csv_data["season"] = season_str
            # print()
            data_list.append(csv_data)
        result = pd.concat(data_list,ignore_index=True)
        # print(result)
        result.to_csv(self.dictionary+"report_data.csv")

if __name__ == '__main__':
    # 季度报表下载器
    # season_report_downloader()
    # 合并季度报告到一个文件里
    Unioner().union()
    pass