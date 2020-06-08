import baostock as bs
import pandas as pd

from baostock.common.contants import BSERR_SUCCESS
from com.fishblack.open.stock.client.StockException import StockException


class StockAPI:

    def __init__(self):
        self.version = 1.0

    def login(self):
        lg = bs.login()
        if lg.error_code == BSERR_SUCCESS:
            print('login respond error_code:' + lg.error_code)
            print('login respond  error_msg:' + lg.error_msg)
            return
        else:
            raise StockException('Error when login into BaoStock[error_code:' + lg.error_code + ' errors:' + lg.error_msg + ']')