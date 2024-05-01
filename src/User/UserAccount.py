from sqlalchemy import ForeignKey

from src.BaseUser.BaseUser import BaseUser, Column, String, Integer
from sqlalchemy.orm import relationship
from src.Tariffs.Tariff import Tariff
from src.Tools.MyHashFunc import HashFunction


class UserAccount(BaseUser):
    id = Column(Integer, primary_key=True)
    tariff_id = Column(Integer, ForeignKey('tariff.id'))

    def __init__(self, first_name: str, last_name: str, birth_date: str,
                 passport_id: str, sex: str, username: str, password: str,
                 phone_number: str, main_tariff: Tariff, gb=0, minutes=0, balance=0) -> None:
        super().__init__(first_name, last_name, birth_date, passport_id, sex)
        self.username = username
        self.password = HashFunction.sha256_str(password)
        self.phone_number = phone_number
        self.gb = 0
        self.minutes = 0
        self.balance = 0
        self.main_tariff = main_tariff

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_phone_number(self) -> str:
        return self.phone_number

    def get_gb(self) -> int:
        return self.gb

    def set_gb(self, value: int) -> None:
        self.gb = value

    def get_minutes(self) -> int:
        return self.minutes

    def set_minutes(self, value: int) -> None:
        self.minutes = value

    def get_balance(self) -> int:
        return self.balance

    def set_balance(self, value: int) -> None:
        self.balance = value

    def share_gb(self, other, value: int) -> str:
        if self.get_gb() >= value:
            other.set_gb(other.get_gb() + value)
            self.set_gb(self.get_gb() - value)
            return "Успешно!"
        else:
            return "Недостаточно гигабайтов на балансе"

    def share_minute(self, other, value: int) -> str:
        if self.get_minutes() >= value:
            other.set_minutes(other.get_minutes() + value)
            self.set_minutes(self.get_minutes() - value)
            return "Успешно!"
        else:
            return "Недостаточно минут на балансе"

    def deposit(self, money: int) -> None:
        self.set_balance(self.get_balance() + money)

    def get_tariff(self) -> Tariff:
        return self.main_tariff

    def pay_tariff(self):
        if self.get_tariff().get_price() >= self.get_balance():
            return False
        self.set_gb(self.get_gb() + self.get_tariff().get_gb())
        self.set_minutes(self.get_minutes() + self.get_tariff().get_minutes())
        self.set_balance(self.get_balance() - self.get_tariff().get_price())
        return True

    def set_tariff(self, new_tariff: Tariff) -> None:
        self.main_tariff = new_tariff

    def buy_gb(self, value: int) -> str:
        if self.get_balance() >= self.get_tariff().get_cost_one_gb() * value:
            self.set_gb(self.get_gb() + value)
            self.set_balance(self.get_balance() - self.get_tariff().get_cost_one_gb() * value)
            return True
        else:
            return False

    def buy_minute(self, value: int) -> str:
        if self.get_balance() >= self.get_tariff().get_cost_one_minute() * value:
            self.set_minutes(self.get_minutes() + value)
            self.set_balance(self.get_balance() - self.get_tariff().get_cost_one_minute() * value)
            return True
        else:
            return False

    def change_number(self, new_number: str) -> None:
        self.phone_number = new_number

    username = Column(String(1000), unique=True)
    password = Column(String(1000), unique=False)
    phone_number = Column(String(15), unique=True)
    gb = Column(Integer, unique=False)
    minutes = Column(Integer, unique=False)
    balance = Column(Integer, unique=False)
    main_tariff = relationship("Tariff")
    __tablename__ = 'user_account'
