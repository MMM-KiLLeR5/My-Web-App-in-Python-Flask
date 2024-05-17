import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BaseUser.BaseUser import Base
from User.UserAccount import UserAccount, HashFunction
from Tariffs.Tariff import Tariff


class TestUserAccount(unittest.TestCase):
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)

    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_user_account_creation(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user = UserAccount("John", "Doe", "1990-01-01", "1234567890", "male", "barry_allen", "password", "987654321",
                           tariff)
        self.session.add(user)
        self.session.commit()
        queried_user = self.session.query(UserAccount).filter_by(username="barry_allen").first()
        self.assertEqual(queried_user.get_username(), "barry_allen")
        self.assertEqual(queried_user.get_password(), HashFunction.sha256_str("password"))
        self.assertEqual(queried_user.get_phone_number(), "987654321")
        self.assertEqual(queried_user.get_gb(), 0)
        self.assertEqual(queried_user.get_minutes(), 0)
        self.assertEqual(queried_user.get_balance(), 0)
        self.assertEqual(queried_user.get_tariff(), tariff)

    def test_buy_gb(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user = UserAccount("Barry", "Allen", "1990-01-01", "1234567890", "male", "barry_allen", "password", "987654321",
                           tariff)
        user.deposit(1000)
        self.assertTrue(user.buy_gb(10))
        self.assertEqual(user.get_gb(), 10)
        self.assertEqual(user.get_balance(), 950)
        user.set_balance(10)
        self.assertFalse(user.buy_gb(10))
        self.assertEqual(user.get_gb(), 10)
        self.assertEqual(user.get_balance(), 10)

    def test_buy_minute(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "987654321",
                           tariff)
        user.deposit(1000)
        self.assertTrue(user.buy_minute(50))
        self.assertEqual(user.get_minutes(), 50)
        self.assertEqual(user.get_balance(), 500)
        user.set_balance(10)
        self.assertFalse(user.buy_minute(50))
        self.assertEqual(user.get_minutes(), 50)
        self.assertEqual(user.get_balance(), 10)

    def test_set_gb(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           tariff)
        user.set_gb(100)
        self.assertEqual(user.get_gb(), 100)

    def test_set_minute(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           tariff)
        user.set_minutes(200)
        self.assertEqual(user.get_minutes(), 200)

    def test_share_gb(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user1 = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                            tariff)
        user2 = UserAccount("Bruce", "Wayne", "19920101", "0987654321", "male", "bruce_wayne", "password", "9876543210",
                            tariff)
        user1.set_gb(100)
        user2.set_gb(50)
        # Can share
        self.assertEqual(user1.share_gb(user2, 50), "Успешно!")
        self.assertEqual(user1.get_gb(), 50)
        self.assertEqual(user2.get_gb(), 100)
        # Cannot share
        self.assertEqual(user1.share_gb(user2, 60), "Недостаточно гигабайтов на балансе")
        self.assertEqual(user1.get_gb(), 50)
        self.assertEqual(user2.get_gb(), 100)

    def test_share_minute(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user1 = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                            tariff)
        user2 = UserAccount("Bruce", "Wayne", "19920101", "0987654321", "male", "bruce_wayne", "password", "9876543210",
                            tariff)
        user1.set_minutes(200)
        user2.set_minutes(100)
        # Can share
        self.assertEqual(user1.share_minute(user2, 50), "Успешно!")
        self.assertEqual(user1.get_minutes(), 150)
        self.assertEqual(user2.get_minutes(), 150)
        # Cannot share
        self.assertEqual(user1.share_minute(user2, 200), "Недостаточно минут на балансе")
        self.assertEqual(user1.get_minutes(), 150)
        self.assertEqual(user2.get_minutes(), 150)

    def test_pay_tariff(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           tariff)
        # Can pay tariff
        user.deposit(600)
        self.assertTrue(user.pay_tariff())
        self.assertEqual(user.get_gb(), 0)
        self.assertEqual(user.get_minutes(), 0)
        self.assertEqual(user.get_balance(), 100)
        # Cannot pay tariff
        user.set_balance(400)
        self.assertFalse(user.pay_tariff())
        self.assertEqual(user.get_gb(), 0)
        self.assertEqual(user.get_minutes(), 0)
        self.assertEqual(user.get_balance(), 400)

    def test_set_tariff(self):
        tariff1 = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        tariff2 = Tariff(cost_one_gb=10, cost_one_minute=20, price=1000)
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           tariff1)
        user.set_tariff(tariff2)
        self.assertEqual(user.get_tariff(), tariff2)

    def test_change_number(self):
        tariff = Tariff(cost_one_gb=5, cost_one_minute=10, price=500)
        user = UserAccount("Barry", "Allen", "19900101", "1234567890", "male", "barry_allen", "password", "1234567890",
                           tariff)
        user.change_number("9876543210")
        self.assertEqual(user.get_phone_number(), "9876543210")


if __name__ == '__main__':
    unittest.main()
