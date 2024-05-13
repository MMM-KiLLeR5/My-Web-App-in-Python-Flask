import unittest
from Tariffs.Tariff import Tariff


class TestTariff(unittest.TestCase):
    def test_tariff_creation(self):
        tariff = Tariff(10, 5, 100, 1, 1)
        self.assertEqual(tariff.get_cost_one_gb(), 10)
        self.assertEqual(tariff.get_cost_one_minute(), 5)
        self.assertEqual(tariff.get_price(), 100)
        self.assertEqual(tariff.get_gb(), 1)
        self.assertEqual(tariff.get_minutes(), 1)

    def test_change_tariff(self):
        tariff = Tariff(10, 5, 100, 1, 1)
        tariff.change_tariff(15, 7, 150, 2, 2)
        self.assertEqual(tariff.get_cost_one_gb(), 15)
        self.assertEqual(tariff.get_cost_one_minute(), 7)
        self.assertEqual(tariff.get_price(), 150)
        self.assertEqual(tariff.get_gb(), 2)
        self.assertEqual(tariff.get_minutes(), 2)

if __name__ == '__main__':
    unittest.main()
