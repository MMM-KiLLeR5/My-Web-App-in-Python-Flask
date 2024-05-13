import unittest
from Tariffs.Tariff import Tariff
from Admin.AdminAccount import AdminAccount, HashFunction


class TestAdminAccount(unittest.TestCase):
    def setUp(self):
        self.user = AdminAccount("Barry", "Allen", "1990-01-01", "1234567890", "male", "admin", "password", "987654321")

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), "admin")

    def test_get_password(self):
        self.assertEqual(self.user.get_password(), HashFunction.sha256_str("password"))

    def test_get_phone_number(self):
        self.assertEqual(self.user.get_phone_number(), "987654321")

    def test_create_tariff(self):
        tariff = self.user.create_tariff(10, 100, 500, 5, 10)
        self.assertIsInstance(tariff, Tariff)

    def test_change_tariff(self):
        tariff = self.user.create_tariff(10, 100, 500, 5, 10)
        self.user.change_tariff(tariff, 15, 150, 750, 7, 12)
        self.assertEqual(tariff.get_cost_one_gb(), 7)
        self.assertEqual(tariff.get_cost_one_minute(), 12)
        self.assertEqual(tariff.get_price(), 750)
        self.assertEqual(tariff.get_gb(), 15)
        self.assertEqual(tariff.get_minutes(), 150)


if __name__ == '__main__':
    unittest.main()
