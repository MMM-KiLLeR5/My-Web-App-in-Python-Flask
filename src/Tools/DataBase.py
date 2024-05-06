from sqlalchemy import create_engine, and_
from src.BaseUser.BaseUser import Base
from sqlalchemy.orm import sessionmaker, defer
from src.Constants import Config


class ControlDataBase:
    def __init__(self, db_url):
        self.__engine = create_engine(db_url, echo=False)
        self.__session = None

    def create_tables(self):
        Base.metadata.create_all(self.__engine)

    def creat_session(self):
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    def drop_tables(self):
        Base.metadata.drop_all(self.__engine)

    def query(self, model):
        return self.__session.query(model)

    def query_with_options(self, model, expressions, column_to_exclude):
        return self.__session.query(model).options(defer(column_to_exclude)).filter(
            expressions).all()

    def find(self, model, expressions):
        return len(self.__session.query(model).filter(and_(*expressions)).all()) != 0

    def insert(self, obj):
        self.__session.add(obj)
        self.__session.commit()

    def delete(self, model, expressions):
        if self.find(model, expressions):
            obj = self.__session.query(model).filter(and_(*expressions)).all()[0]
            self.__session.delete(obj)
            self.__session.commit()
            return
        print("THERE IS NO SUCH OBJECT IN THE DATABASE")  # TODO менять логику

    def get_object(self, model, expressions):
        if self.find(model, expressions):
            obj = self.__session.query(model).filter(and_(*expressions)).all()[0]
            return obj
        print("THERE IS NO SUCH OBJECT IN THE DATABASE")  # TODO менять логику
        return None

    def commit(self):
        self.__session.commit()


# DATABASE_URL = 'postgresql://postgres:123@192.168.0.105:5432/test'
db_url = Config.DATABASE_URL
database = ControlDataBase(db_url)
database.create_tables()
database.creat_session()
