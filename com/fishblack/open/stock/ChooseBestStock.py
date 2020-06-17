import pandas as pd
import datetime
from com.fishblack.open.stock.client import StockException
from com.fishblack.open.stock.client.StockAPI import StockAPI
from com.fishblack.open.stock.utils.StrUtil import StrUtil
from com.fishblack.open.stock import login


bao_stock_client = StockAPI()
str_util = StrUtil()
today = datetime.date.today().strftime('%Y-%m-%d')
#today = '2020-06-15'
quarter_start = '2020-03-01'
quarter_end = '2020-06-15'

if __name__ == '__main__':
    stock_data = bao_stock_client.query_all_stock_code(today)
    print("Total number:" + str(len(stock_data)))
    if stock_data.empty:
        print("Stock Closed, change another date.")
    else:
        data_df = pd.DataFrame()
        for index in stock_data.code.index:
            code = stock_data["code"].get(index)
            if str_util.is_shang_zheng(code=code) or str_util.is_shen_zhen(code=code):
                name = stock_data["code_name"].get(index)
                print("Downloading :" + code + " " + name)

                forecast_rs = bao_stock_client.query_stock_forecast_report_summary(code, quarter_start, quarter_end)
                if len(forecast_rs.data) > 0 and (forecast_rs.data[0][3] == '预增' or forecast_rs.data[0][3] == '略增' or forecast_rs.data[0][3] == '续盈' or forecast_rs.data[0][3] == '扭亏'):
                    k_rs = bao_stock_client.query_history_k_data_plus(code, "code,open,high,low,close,peTTM", today, today,
                                                                      frequency="d", adjustflag="3")
                    industry_rs = bao_stock_client.query_stock_industry(code)
                    industry = ""
                    if len(industry_rs.data) > 0:
                        industry = industry_rs.data[0][3]
                    extend = pd.DataFrame(k_rs.data)
                    extend[6] = name
                    extend[7] = industry
                    extend[8] = forecast_rs.data[0][3]
                    extend[9] = forecast_rs.data[0][4]
                    data_df = data_df.append(extend, ignore_index=True)
                elif len(forecast_rs.data) != 0:
                        print(forecast_rs.data[0][3])

        #data_df = data_df.sort_values(by=6, axis=1)
        #columns = ['代码', '开盘', '最高', '最低', '收盘', '市盈率', '名称', '预估', '总结']
        #result_df = pd.DataFrame(data_df, columns=columns)

        data_df.rename(columns={data_df.columns[0]: "代码"}, inplace=True)
        data_df.rename(columns={data_df.columns[1]: "开盘"}, inplace=True)
        data_df.rename(columns={data_df.columns[2]: "最高"}, inplace=True)
        data_df.rename(columns={data_df.columns[3]: "最低"}, inplace=True)
        data_df.rename(columns={data_df.columns[4]: "收盘"}, inplace=True)
        data_df.rename(columns={data_df.columns[5]: "市盈率"}, inplace=True)
        data_df.rename(columns={data_df.columns[6]: "名称"}, inplace=True)
        data_df.rename(columns={data_df.columns[7]: "行业"}, inplace=True)
        data_df.rename(columns={data_df.columns[8]: "业绩预估"}, inplace=True)
        data_df.rename(columns={data_df.columns[9]: "业绩"}, inplace=True)
        data_df['市盈率'] = pd.to_numeric(data_df['市盈率'])
        data_df['最高'] = pd.to_numeric(data_df['最高'])
        data_df['最低'] = pd.to_numeric(data_df['最低'])
        data_df['收盘'] = pd.to_numeric(data_df['收盘'])
        data_df['开盘'] = pd.to_numeric(data_df['开盘'])
        data_df = data_df[(data_df["市盈率"] < 200) & (data_df["市盈率"] > 10) & ((data_df["收盘"] - data_df["开盘"]) > 0)]
        data_df.sort_values(by="市盈率", ascending=True, inplace=True)
        data_df.to_csv("C:\\Work\\Project\\Python\\openStock\\output\\data\\" + today + "_data.csv", encoding="gbk",
                       index=False)
        print("Finished")

from com.fishblack.open.stock import logout