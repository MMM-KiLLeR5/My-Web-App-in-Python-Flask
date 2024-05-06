from src.User.UserAccount import UserAccount
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.BaseUser.BaseUser import Base


class StockMarket(Base):
    id = Column(Integer, primary_key=True)
    cost = Column(Integer, unique=False, nullable=True)
    gb = Column(Integer, unique=False, nullable=True)
    min = Column(Integer, unique=False, nullable=True)
    user_id = Column(Integer, ForeignKey('user_account.id'))
    user = relationship(UserAccount)
    __tablename__ = 'stock_market'


    def __init__(self, user, cost, gb=0, min=0):
        if gb == 0 and min > user.get_minutes():
            raise ValueError('MIN must be greater than or equal to')
        if min == 0 and gb > user.get_gb():
            raise ValueError('GB must be greater than or equal to')

        self.cost = cost
        self.gb = gb
        self.min = min
        self.user = user
        self.user.set_minutes(user.get_minutes() - min)
        self.user.set_gb(user.get_gb() - gb)


    def buy_gb(self):
        self.gb = 0
        self.user.set_balance(self.user.get_balance + self.cost)

    def buy_min(self):
        self.min = 0
        self.user.set_balance(self.user.get_balance + self.cost)

