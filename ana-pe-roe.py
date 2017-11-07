#-*- coding:utf-8 -*-

# 分析沪深上市公司各个股票的 市盈率（pe） 和 最近几个季度的 净资产收益率
import pandas as pd
import numpy as np
import csv
from datetime import datetime
class Ana_pe_roe():
    def __init__(self):
        # self.hs_stocks = pd.read_csv('./data/HS_stocks_basic_info.csv', dtype={"code": np.str})
        # self.hs_stocks = pd.read_csv('./data/HS_stocks_2017_09_21.csv', dtype={"code": np.str})
        self.hs_stocks = pd.read_csv('./data/HS_stocks_2017_09_24.csv', dtype={"code": np.str})
        self.season_report = pd.read_csv("./data/report_data/report_data.csv", dtype={"code": np.str}, index_col=0)

        self.min_season = 20163    # 在此之后的市盈率
        self.max_season = 20172    # 在此之后的市盈率
        self.season_list = []
        min_year , min_season = int(str(self.min_season)[:-1]),int(str(self.min_season)[-1])
        for year in range(min_year,2018):
            for season in range(1,5):
                new_season = year * 10 + season
                if new_season >= self.min_season and new_season<=self.max_season:
                    self.season_list .append(new_season)
        print(self.season_list)

    # 读取一下沪深上市公司的基本信息
    # def read_file(self,filename):
    #     result =
    #     return result

    def loop_report(self):
        stock_pe_roe_list = [["code","name","industry","area","市盈率(pe)","每股收益(eps)","市净率(pb)","每股净资产(bvps)","股价(pe*eps)","股价(pb*bvps)","净资产收益(roe)"]]
        stock_pe_roe_list[0].extend(self.season_list)
        all_count = len(self.hs_stocks)
        handled = 0
        for _index , a_stock in self.hs_stocks.iterrows():
            handled += 1
            print("进度:{0}/{1}".format(handled,all_count))
            a_pe_roe = []
            # 股票的代码
            _code =a_stock["code"]
            _name = a_stock["name"]
            _industry = a_stock["industry"]
            _area = a_stock["area"]
            _pe = a_stock["pe"] # 市盈率
            _eps = a_stock["esp"]   # 每股收益
            _pb = a_stock["pb"] # 市净率
            _bvps = a_stock["bvps"] # 每股净资产

            try:
                _price_pe = _pe *_eps # 根据市盈率计算股价
            except:
                _price_pe = ''

            try:
                _price_pb = _pb *_bvps # 根据市净率计算股价
            except:
                _price_pb = ''

            # roe 当前每股净资产收益率
            try:
                _roe_now = 100 * _pb / _pe*2    # 这里pe貌似是错误的，除以2就正常了许多
            except:
                _roe_now = ''
            a_pe_roe.extend([_code,_name,_industry,_area,_pe ,_eps, _pb , _bvps,_price_pe , _price_pb,_roe_now])
            # 从财务报告筛选出股票近四个季度的roe
            _roe = self.season_report[(self.season_report.code == _code) & (self.season_report.season >= self.min_season)][["roe", "season"]]
            roe_dic = {}
            for _ , _row in _roe.iterrows():
                roe_dic[int(_row["season"])] = _row["roe"]
            for roe_season in self.season_list:
                a_pe_roe.append(roe_dic.get(roe_season,""))
            stock_pe_roe_list.append(a_pe_roe)
        print(stock_pe_roe_list)
        with open("./data/Ana_pe-roe-pb_{0}.csv".format(datetime.now().strftime("%Y_%m_%d")),"w") as f:
            csv_writer= csv.writer(f)
            for row in stock_pe_roe_list:
                csv_writer.writerow(row)
        return stock_pe_roe_list

if __name__ == '__main__':
    Ana_pe_roe().loop_report()