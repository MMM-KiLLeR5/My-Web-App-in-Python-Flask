from src.User.UserAccount import UserAccount, Tariff
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
        if (gb > user.get_gb()):
            raise ValueError('GB cannot be greater than user.get_gb()')
        if (min > user.get_minutes()):
            raise ValueError('MIN cannot be greater than user.get_min()')

        self.cost = cost


    def buy_gb(self):
        self.gb = 0
        self.user.balance += self.cost

    def buy_min(self):
        self.min = self = 0
        self.user.balance += self.cost

