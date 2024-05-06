from src.Market.StockMarket import StockMarket
from src.User.UserAccount import UserAccount
from src.Tools.DataBase import database


class Handler:
    key_for_min = []
    key_for_gb = []

    @staticmethod
    def create_min_offer(username, cost, min):
        Handler.__create_offer(username, cost, min, 0)

    @staticmethod
    def create_gb_offer(username, cost, gb):
        Handler.__create_offer(username, cost, 0, gb)

    @staticmethod
    def get_minutes_market():
        market = sorted(database.query_with_options(StockMarket, (StockMarket.min > 0), StockMarket.gb),
                        key=lambda item: item.min / item.cost, reverse=True)
        Handler.key_for_min = []
        for item in market:
            Handler.key_for_min.append(item.id)
        return market

    @staticmethod
    def get_gb_market():
        market = sorted(database.query_with_options(StockMarket, (StockMarket.gb > 0), StockMarket.gb),
                        key=lambda item: (Handler, item.gb / item.cost), reverse=True)
        Handler.key_for_gb = []
        for item in market:
            Handler.key_for_gb.append(item.id)
        return market

    @staticmethod
    def buy_gb(username, id):
        products = Handler.__take_usernames_money(username, Handler.key_for_gb[id - 1])
        if products is None:
            return True
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        user.set_gb(user.get_gb() + products.gb)
        products.buy_gb()
        database.delete(StockMarket, (StockMarket.id == Handler.key_for_gb[id - 1], True))
        Handler.key_for_gb.pop(id - 1)

    @staticmethod
    def buy_minutes(username, id):
        products = Handler.__take_usernames_money(username, Handler.key_for_min[id - 1])
        if products is None:
            return True
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        user.set_minutes(user.get_minutes() + products.min)
        products.buy_min()
        database.delete(StockMarket, (StockMarket.id == Handler.key_for_min[id - 1], True))
        Handler.key_for_min.pop(id - 1)


    @staticmethod
    def __take_usernames_money(username, id):
        products = database.get_object(StockMarket, (StockMarket.id == id, True))
        cost = products.cost
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        if (user.get_balance() < cost):
            return
        user.set_balance(user.get_balance() - cost)
        return products

    @staticmethod
    def __create_offer(username, cost, min, gb):
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        offer = StockMarket(user, cost, gb, min)
        database.insert(offer)
