# _*_ coding:utf-8 _*_


"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10 * 0.01；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10 * 0.01提成，高于10万元的部分，可可提
　　　成7.5 * 0.01；20万到40万之间时，高于20万元的部分，可提成5 * 0.01；40万到60万之间时高于
　　　40万元的部分，可提成3 * 0.01；60万到100万之间时，高于60万元的部分，可提成1.5 * 0.01，高于
　　　100万元时，超过100万元的部分按1 * 0.01提成，从键盘输入当月利润I，求应发放奖金总数？
"""
"""
分析：
    I≤10    10 * 0.01
10＜I≤20    7.5 * 0.01
20＜I≤40    5 * 0.01
40＜I≤60    3 * 0.01
60＜I≤100   1.5 * 0.01
100＜I       1 * 0.01
"""

# 键入利润profit
profit = int(input("输入利润(万元)：\n"))

# define rate
rate_1 = 0.1
rate_2 = 0.075
rate_3 = 0.05
rate_4 = 0.03
rate_5 = 0.015
rate_6 = 0.01
# 计算提成commission
if profit <= 10:
    commission = profit * rate_1
elif profit <= 20:
    commission = 10 * rate_1 + (profit - 10) * rate_2
elif profit <= 40:
    commission = 10 * rate_1 + (20 - 10) * rate_2 + (profit-20) * rate_3
elif profit <= 60:
    commission = 10 * rate_1 + (20 - 10) * rate_2 + (40 - 20) * rate_3 + (profit - 40) * rate_4
elif profit <= 100:
    commission = 10 * rate_1 + (20 - 10) * rate_2 * 0.01 + (40 - 20) * rate_3 + (60 - 40) * rate_4 + \
                 (profit - 60) * rate_5
elif profit > 100:
    commission = 10 * rate_1 + (20 - 10) * rate_2 + (40 - 20) * rate_3 + (60 - 40)*rate_4 + \
                 (100 - 60) * rate_5 + (profit-100) * rate_6

print("commission:", commission)
