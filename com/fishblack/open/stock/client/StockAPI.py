import baostock as bs
import datetime
from baostock.common.contants import BSERR_SUCCESS
from com.fishblack.open.stock.client.StockException import StockException


class StockAPI:

    def __init__(self):
        self.version = 1.0

    # anonymous login
    def login(self):
        lg = bs.login()
        if lg.error_code == BSERR_SUCCESS:
            print('login respond error_code:' + lg.error_code)
            print('login respond  error_msg:' + lg.error_msg)
            return
        else:
            raise StockException('Error when login into BaoStock[error_code:' + lg.error_code + ' errors:' + lg.error_msg + ']')

    # anonymous logout
    def logout(self):
        lg = bs.logout()
        pass

    # 获取股票代码
    def query_all_stock_code(self, date):
        stock_rs = bs.query_all_stock(date)
        stock_data = stock_rs.get_data()
        return stock_data

    def query_history_k_data_plus(self, code, columns, start_date, end_date, frequency, adjustflag):
        stock_k_data = bs.query_history_k_data_plus(code, columns, start_date, end_date, frequency, adjustflag)
        return stock_k_data

    def query_hangye(self):
        pass

    def query_stock_forecast_report_summary(self, code, start_date, end_date):
        forecast_report_data = bs.query_forecast_report(code, start_date=start_date, end_date=end_date)
        return forecast_report_data


