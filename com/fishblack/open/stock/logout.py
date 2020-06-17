from com.fishblack.open.stock.client.StockAPI import StockAPI
from com.fishblack.open.stock.client import StockException

bao_stock_client = StockAPI()
try:
    bao_stock_client.logout()
except StockException as e:
    print(e)