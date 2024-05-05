# -*- coding: utf-8 -*-
from src.Admin.AdminAccount import AdminAccount, Tariff
from src.Tools.DataBase import database
from flask_jwt_extended import create_access_token
from datetime import timedelta
from src.Tools.MyHashFunc import sha256


class HandleAdmin(AdminAccount):
    @staticmethod
    def create_admin_account(**kwargs):
        admin = AdminAccount(**kwargs)
        database.insert(admin)
        return HandleAdmin.get_token(admin)

    @staticmethod
    def get_admin(username, password):
        admin = database.get_object(AdminAccount, (AdminAccount.get_username(AdminAccount) == username,
                                                   AdminAccount.get_password(AdminAccount) == sha256(password)))
        return admin

    @staticmethod
    def is_admin(methods, attribute):
        getter = {'username': AdminAccount.get_username,
                  'passport_id': AdminAccount.get_passport_id,
                  'phone_number': AdminAccount.get_phone_number
                  }
        return database.find(AdminAccount, (getter[methods](AdminAccount) == attribute, True))

    @staticmethod
    def create_new_tariff(**kwargs):
        new_tariff = AdminAccount.create_tariff(**kwargs)

        database.insert(new_tariff)

    @staticmethod
    def update_tariffs(tariff_id, **kwargs):
        tariff = database.get_object(Tariff, (Tariff.id == tariff_id, True))
        if tariff is None:
            return
        AdminAccount.change_tariff(tariff, **kwargs)
        return True

    @staticmethod
    def get_token(admin, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=admin.get_username(), expires_delta=expire_delta, additional_claims={'role': 'admin'})
        return token

    @staticmethod
    def get_list_of_tariffs():
        list_of_tariff = database.query(Tariff)
        return list_of_tariff

    @staticmethod
    def get_tariff_by_id(tariff_id):
        tariff = database.get_object(Tariff, (Tariff.id == tariff_id, True))
        return tariff
