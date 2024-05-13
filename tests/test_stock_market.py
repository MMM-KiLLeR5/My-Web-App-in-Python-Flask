import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BaseUser.BaseUser import Base
from User.UserAccount import UserAccount
from Tariffs.Tariff import Tariff
from Market.StockMarket import StockMarket


class TestStockMarket(unittest.TestCase):
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)

    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_stock_market_creation_with_enough_gb(self):
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           Tariff(cost_one_gb=5, cost_one_minute=10, price=500))
        user.gb = 10
        self.session.add(user)
        self.session.commit()
        user = self.session.query(UserAccount).filter_by(username="barry_allen").first()
        stock = StockMarket(user, 200, 5, 0)
        self.assertEqual(stock.cost, 200)
        self.assertEqual(stock.gb, 5)
        self.assertEqual(stock.min, 0)

    def test_stock_market_creation_with_not_enough_gb(self):
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           Tariff(cost_one_gb=5, cost_one_minute=10, price=500))
        self.session.add(user)
        self.session.commit()
        user = self.session.query(UserAccount).filter_by(username="barry_allen").first()
        with self.assertRaises(ValueError) as context:
            StockMarket(user, 200, 10, 0)
        self.assertTrue('GB must be greater than or equal to' in str(context.exception))

    def test_stock_market_creation_with_enough_minutes(self):
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           Tariff(cost_one_gb=5, cost_one_minute=10, price=500))
        user.minutes = 10
        self.session.add(user)
        self.session.commit()
        user = self.session.query(UserAccount).filter_by(username="barry_allen").first()
        stock = StockMarket(user, 200, 0, 5)
        self.assertEqual(stock.cost, 200)
        self.assertEqual(stock.gb, 0)
        self.assertEqual(stock.min, 5)

    def test_stock_market_creation_with_not_enough_minutes(self):
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           Tariff(cost_one_gb=5, cost_one_minute=10, price=500))
        self.session.add(user)
        self.session.commit()
        user = self.session.query(UserAccount).filter_by(username="barry_allen").first()
        with self.assertRaises(ValueError) as context:
            StockMarket(user, 200, 0, 10)
        self.assertTrue('MIN must be greater than or equal to' in str(context.exception))

    def test_buy_gb(self):
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           Tariff(cost_one_gb=5, cost_one_minute=10, price=500))
        user.balance = 300
        user.gb = 5
        self.session.add(user)
        self.session.commit()
        user = self.session.query(UserAccount).filter_by(username="barry_allen").first()
        stock = StockMarket(user, 200, 5, 0)
        stock.buy_gb()
        self.assertEqual(stock.gb, 0)
        self.assertEqual(user.get_balance(), 500)

    def test_buy_min(self):
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           Tariff(cost_one_gb=5, cost_one_minute=10, price=500))
        user.balance = 300
        user.minutes = 5
        self.session.add(user)
        self.session.commit()
        user = self.session.query(UserAccount).filter_by(username="barry_allen").first()
        stock = StockMarket(user, 200, 0, 5)
        stock.buy_min()
        self.assertEqual(stock.min, 0)
        self.assertEqual(user.get_balance(), 500)
