from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseUser(Base):
    id = Column(Integer, primary_key=True)

    def __init__(self, first_name: str, last_name: str,
                 birth_date: str, passport_id: str, sex: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.passport_id = passport_id
        self.sex = sex

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_birth_data(self) -> str:
        return self.birth_date

    def get_passport_id(self) -> str:
        return self.passport_id

    def get_sex(self) -> str:
        return self.sex

    __abstract__ = True
    first_name = Column(String(50), unique=False)
    last_name = Column(String(50), unique=False)
    birth_date = Column(String(15), unique=False)
    passport_id = Column(String(15), unique=True, nullable=False)
    sex = Column(String(1), unique=False)
