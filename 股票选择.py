#-*- coding:utf-8 -*-

import tushare as ts
import datetime

# 股票列表
'''
获取沪深上市公司基本情况。属性包括：

code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数

调用方法：
import tushare as ts
ts.get_stock_basics()
'''

basic_stocks_HS = ts.get_stock_basics()
basic_stocks_HS.to_csv("./data/HS_stocks_{0}.csv".format(datetime.datetime.now().strftime("%Y_%m_%d")))
