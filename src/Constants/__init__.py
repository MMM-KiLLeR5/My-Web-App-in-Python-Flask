import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    KNOWN_HOST = os.environ.get("KNOWN_HOST")
    PORT = os.environ.get("PORT")


class AdminErrorMessages:
    NON_EXISTING_ADMIN = "Admin not found"
    NON_EXISTING_TARIFF = "No such tariff"


class AdminApprovalMessages:
    EDIT_TARIFF_SUCCESSFULLY = "Tariff edited successfully"
    CREATE_TARIFF_SUCCESSFULLY = "Tariff created successfully"


class UserErrorMessages:
    NON_EXISTING_USER = "User not found"
    NON_EXISTING_TARIFF = "No such tariff"
    NON_EXISTING_USER_WITH_PHONE_NUMBER = "There is no user with this phone_number"
    NOT_ENOUGH_GB = "Not enough gb"
    NOT_ENOUGH_MINUTE = "Not enough minute"
    NOT_ENOUGH_MONEY = "Not enough money"


class UserApprovalMessages:
    EDIT_TARIFF_SUCCESSFULLY = "Success"
    CHANGE_TARIFF_SUCCESSFULLY = "Success"
    CREATE_TARIFF_SUCCESSFULLY = "Success"
    REGISTER_USER_SUCCESSFULLY = "Success"
    GB_SHARED_SUCCESSFULLY = "Success"
    MINUTE_SHARED_SUCCESSFULLY = "Success"
    GB_BOUGHT_SUCCESSFULLY = "Success"
    MINUTE_BOUGHT_SUCCESSFULLY = "Success"
    DEPOSIT_SUCCESSFULLY = "Success"
    PAID_TARIFF_SUCCESSFULLY = "Success"
    GB_OFFERED_SUCCESSFULLY = "Success"
    MINUTE_OFFERED_SUCCESSFULLY = "Success"
