import unittest
from unittest.mock import MagicMock, patch
from Admin.AdminAccount import AdminAccount, Tariff
from User.UserAccount import UserAccount
from Tools.DataBase import ControlDataBase


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = ControlDataBase('sqlite:///:memory:')
        self.database.create_tables()
        self.database.creat_session()
        self.tariff = Tariff(1, 1, 1, 1, 1)
        self.user = UserAccount('1', '1', '1', '1', '1', '1', '1', '1', self.tariff)
        self.admin = AdminAccount('1', '1', '1', '1', '1', '1', '1', '1')

    def test_drop_table(self):
        self.database.drop_tables()
        self.database.create_tables()

    def test_add(self):
        self.database.insert(self.tariff)
        self.database.insert(self.admin)
        self.database.insert(self.user)
        self.assertEqual(self.admin,
                         self.database.get_object(AdminAccount, (AdminAccount.get_username(AdminAccount) == '1', True)))

    def test_delete(self):
        assert self.database.delete(AdminAccount, (AdminAccount.get_username(AdminAccount) == '2', True)) is None

    def test_delete_2(self):
        self.database.insert(self.admin)
        assert self.database.delete(AdminAccount, (AdminAccount.get_username(AdminAccount) == '1', True)) is None

    def test_commit(self):
        assert self.database.commit() is None

    def test_query(self):
        self.database.insert(self.tariff)
        self.assertEqual(self.database.query(Tariff)[0], self.tariff)

    def test_query_2(self):
        self.database.insert(self.tariff)
        self.database.creat_session()
        self.assertEqual(self.database.query_with_options(Tariff, True, Tariff.id)[0].gb, 1)

    def test_get(self):
        assert self.database.get_object(Tariff, (Tariff.gb == 2, True)) is None



