from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from storage.tables import ORMBase
from storage.tables.vuln_task import *
from config import *
class StorageManager:
    def __init__(self):

        self.__engine=self.__create_engine(STORAGE_BACKEND)
        self.__session=self.__create_session()

    def __create_engine(self,storage_backend):
        return create_engine(storage_backend,echo=True)

    def __create_session(self):
        return sessionmaker(bind=self.__engine)()

    @property
    def Engine(self):
        return self.__engine

    @property
    def Session(self):
        return self.__session

    def init_db(self):
        ORMBase.metadata.create_all(self.Engine)

    def drop_all(self):
        ORMBase.metadata.drop_all(self.Engine)

    def save(self):
        self.Session.commit()





