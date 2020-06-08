import baostock as bs
import pandas as pd

from com.fishblack.open.stock.client import StockException
from com.fishblack.open.stock.client.StockAPI import StockAPI
import os

#### 登陆系统 ####
try:
    StockAPI().login()
except StockException as e:
    print(e)

stockP = "sz"
stockCode = "002635"
rs = bs.query_history_k_data_plus(stockP + "." + stockCode,
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='2020-06-01', end_date='2020-06-05',
    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
#### 结果集输出到csv文件 ####
result.to_csv("C:\\Work\\Project\\Python\\openStock\\output\\data\\"+stockP+"_"+stockCode+"_data.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
try:
    StockAPI().logout()
except StockException as e:
    print(e)
