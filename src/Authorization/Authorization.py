from User.UserAccount import UserAccount
from Admin.AdminAccount import AdminAccount
from Market.StockMarket import StockMarket
from Tools.DataBase import database
from Tools.MyHashFunc import HashFunction


class Authorization:
    @staticmethod
    def admin_login(username, password):
        password = HashFunction.sha256_str(password)
        if database.find(AdminAccount, (
                AdminAccount.get_username(AdminAccount) == username,
                AdminAccount.get_password(AdminAccount) == password)):
            return database.get_object(AdminAccount, (
                AdminAccount.get_username(AdminAccount) == username,
                AdminAccount.get_password(AdminAccount) == password))

    @staticmethod
    def user_login(username, password):
        password = HashFunction.sha256_str(password)
        if database.find(UserAccount, (
                UserAccount.get_username(UserAccount) == username,
                UserAccount.get_password(UserAccount) == password)):
            return database.get_object(UserAccount, (
                UserAccount.get_username(UserAccount) == username,
                UserAccount.get_password(UserAccount) == password))
