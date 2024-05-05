from src.Market.StockMarket import StockMarket
from src.Tools.DataBase import database

class Handler:
    @staticmethod
    def get_minutes_market():
        market = database.query(StockMarket, (StockMarket.min > 0), StockMarket.gb)
        return market

    @staticmethod
    def get_gb_market():
        market = database.query_with_options(StockMarket, (StockMarket.gb > 0), StockMarket.min)
        return market

    @staticmethod
    def buy_gb(id):
        products = database.get_object(StockMarket, StockMarket.id == id)
        products.buy_gb

    @staticmethod
    def buy_minutes(id):
        products = database.get_object(StockMarket, StockMarket.id == id)
        products.buy_min


