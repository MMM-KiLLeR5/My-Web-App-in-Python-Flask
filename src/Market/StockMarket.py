from src.User.UserAccount import UserAccount, Tariff
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.BaseUser.BaseUser import Base


class StockMarket(Base):
    id = Column(Integer, primary_key=True)
    cost_gb = Column(Integer, unique=False, nullable=True)
    cost_min = Column(Integer, unique=False, nullable=True)
    gb = Column(Integer, unique=False, nullable=True)
    min = Column(Integer, unique=False, nullable=True)
    user_id = Column(Integer, ForeignKey('user_account.id'))
    user = relationship(UserAccount)
    __tablename__ = 'stock_market'


    def __init__(self, user, cost_gb=0, cost_min=0, gb=0, min=0):
        if (gb > user.get_gb()):
            raise ValueError('GB cannot be greater than user.get_gb()')
        if (min > user.get_minutes()):
            raise ValueError('MIN cannot be greater than user.get_min()')

        self.cost_gb = cost_gb
        self.cost_min = cost_min


    def buy_gb(self):
        self.gb = 0
        self.user.balance += self.cost_gb

    def buy_min(self):
        self.min = self = 0
        self.user.balance += self.cost_min

obj = StockMarket(UserAccount('1', '1', '1', '1', '1', '1', '1', '1', Tariff(1, 1, 1, 1, 1)))