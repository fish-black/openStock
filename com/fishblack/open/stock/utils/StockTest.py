import pandas as pd
import datetime
from com.fishblack.open.stock.client import StockException
from com.fishblack.open.stock.client.StockAPI import StockAPI

bao_stock_client = StockAPI()
today = datetime.date.today().strftime('%Y-%m-%d')

try:
    bao_stock_client.login()
except StockException as e:
    print(e)

stock_data = bao_stock_client.query_all_stock_code(today)
print("Total number:" + str(len(stock_data)))

for index in stock_data.code.index:
    code = stock_data["code"].get(index)
    name = stock_data["code_name"].get(index)
    print("Downloading :" + code + " " + name)

    k_rs = bao_stock_client.query_history_k_data_plus(code, "date,code,open,high,low,close", today, today)
    data_df = pd.DataFrame()
    data_df = data_df.append(k_rs.get_data())
    data_df.to_csv("C:\\Work\\Project\\Python\\openStock\\output\\data\\" + code + "_data.csv", encoding="gbk", index=False)

try:
    bao_stock_client.logout()
except StockException as e:
    print(e)
