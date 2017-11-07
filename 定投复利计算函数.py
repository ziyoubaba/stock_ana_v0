#-*- coding:utf-8 -*-

# 定投复利计算
# 例如： 一只股票，每年定投2万，平均每年盈利率15%,15年后的总额

def automatic_invest( money , earn_rate , times):   # 每年定投金额，收益率，定投年份
    #
    invest_money_everytime = money
    invest_money = money    # 总投入金额
    for i in range(times):
        if i+1<times:
            invest_money += invest_money_everytime
            money += money * earn_rate + invest_money_everytime # 本金+利息 + 下一年投入
        else:
            # 最后一年不再投入
            money += money * earn_rate

        # print(money)
    return money,invest_money

# t0 = automatic_invest(1 , 0.15 , 1)
# print(t0)
