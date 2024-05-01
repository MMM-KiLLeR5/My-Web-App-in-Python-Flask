from sqlalchemy import Column, Integer
from src.BaseUser.BaseUser import Base


class Tariff(Base):
    id = Column(Integer, primary_key=True)

    def __init__(self, cost_one_gb: int, cost_one_minute: int,
                 price: int, gb: int = 0, minute: int = 0, ) -> None:
        self.cost_one_gb = cost_one_gb
        self.cost_one_minute = cost_one_minute
        self.gb = gb
        self.minute = minute
        self.price = price

    def change_tariff(self, cost_one_gb: int, cost_one_minute: int,
                      price: int, gb: int = 0, minute: int = 0) -> None:
        self.cost_one_gb = cost_one_gb
        self.cost_one_minute = cost_one_minute
        self.gb = gb
        self.minute = minute
        self.price = price

    def get_cost_one_gb(self) -> int:
        return self.cost_one_gb

    def get_cost_one_minute(self) -> int:
        return self.cost_one_minute

    def get_gb(self):
        return self.gb

    def get_minutes(self):
        return self.minute

    def get_price(self):
        return self.price

    __tablename__ = 'tariff'
    cost_one_gb = Column(Integer, unique=False, nullable=True)
    cost_one_minute = Column(Integer, unique=False, nullable=True)
    gb = Column(Integer, unique=False, nullable=True)
    minute = Column(Integer, unique=False, nullable=True)
    price = Column(Integer, unique=False, nullable=True)
