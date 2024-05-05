from src.Market.StockMarket import StockMarket
from src.User.UserAccount import UserAccount
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
    def buy_gb(username, id):
        products = database.get_object(StockMarket, StockMarket.id == id)
        cost = products.cost
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        user.set_balance(user.get_balance() - cost)
        products.buy_gb()

    @staticmethod
    def buy_minutes(username, id):
        products = database.get_object(StockMarket, StockMarket.id == id)
        cost = products.cost
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        user.set_balance(user.get_balance() - cost)
        products.buy_min()
