from User.UserAccount import UserAccount, Tariff
from Tools.DataBase import database
from flask_jwt_extended import create_access_token
from datetime import timedelta


class HandleUser(UserAccount):
    @staticmethod
    def get_token(user, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=user.get_username(), expires_delta=expire_delta, additional_claims={'role': 'user'})
        return token

    @staticmethod
    def create_user_account(**kwargs):
        tariff = database.get_object(Tariff, (Tariff.id == kwargs['tariff_id'], True))
        kwargs.pop('tariff_id')
        kwargs['main_tariff'] = tariff
        user = UserAccount(**kwargs)
        database.insert(user)
        return HandleUser.get_token(user)

    @staticmethod
    def show_user_details(username, phone_number=''):
        if (username == '' and phone_number == ''):
            raise AttributeError('Does not give proper argument')
        if phone_number == '':
            user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        else:
            user = database.get_object(UserAccount, (UserAccount.get_phone_number(UserAccount) == phone_number, True))
        if user is None:
            return None
        data = {}
        data['user_minutes'] = user.get_minutes()
        data['balance'] = user.get_balance()
        data['user_gbs'] = user.get_gb()
        data['gb'] = user.get_tariff().get_gb()
        data['minute'] = user.get_tariff().get_minutes()
        data['cost_one_minute'] = user.get_tariff().get_cost_one_minute()
        data['cost_one_gb'] = user.get_tariff().get_cost_one_gb()
        data['price'] = user.get_tariff().get_price()
        return data

    @staticmethod
    def share_gb_with_friend(username, phone_number, value):
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        if user is None:
            return None
        if user.get_gb() <= value:
            return False
        if HandleUser.__share_with_friend(user.share_gb, phone_number, value) is None:
            return None
        database.insert(user)
        return True

    @staticmethod
    def share_minute_with_friend(username, phone_number, value):
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        if user is None:
            return None
        if user.get_minutes() <= value:
            return False
        if HandleUser.__share_with_friend(user.share_minute, phone_number, value) is None:
            return None
        database.insert(user)
        return True

    @staticmethod
    def deposit_money(username, value):
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        user.deposit(value)
        database.insert(user)

    @staticmethod
    def change_tariff(username, tariff_id):
        tariff = database.get_object(Tariff, (Tariff.id == tariff_id, True))
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        if tariff is None:
            return True
        user.set_tariff(tariff)
        database.insert(user)
        return False

    @staticmethod
    def handle_buy_gb(username, value):
        return HandleUser.__handle_buy_traffic(username, value, 'buy_gb')

    @staticmethod
    def handle_buy_minute(username, value):
        return HandleUser.__handle_buy_traffic(username, value, 'buy_min')

    @staticmethod
    def user_pay_tariff(username):
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        if user is None:
            return None
        res = user.pay_tariff()
        if res:
            database.insert(user)
        return res

    @staticmethod
    def __share_with_friend(share_function, phone_number, value):
        owner_of_number = database.get_object(UserAccount, (
            UserAccount.get_phone_number(UserAccount) == phone_number, True))
        if owner_of_number is None:
            return None
        share_function(owner_of_number, value)
        database.insert(owner_of_number)
        return True

    @staticmethod
    def is_user(methods, attribute):
        getter = {'username': UserAccount.get_username,
                  'passport_id': UserAccount.get_passport_id,
                  'phone_number': UserAccount.get_phone_number
                  }
        return database.find(UserAccount, (getter[methods](UserAccount) == attribute, True))

    @staticmethod
    def __handle_buy_traffic(username, value, buy_func_key):
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        buy_func = {
            'buy_gb': user.buy_gb,
            'buy_min': user.buy_minute
        }
        res = buy_func[buy_func_key](value)
        if res:
            database.insert(user)
        return res
