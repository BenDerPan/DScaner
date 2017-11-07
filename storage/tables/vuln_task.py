from sqlalchemy import Table, MetaData, Column, Integer, String, Text
from sqlalchemy.orm import mapper
from storage.tables import ORMBase
import datetime


class VulnTask(ORMBase):
    __tablename__="vulntask"
    id=Column(Integer,primary_key=True)
    target=Column(String(512))
    target_id=Column(String(128))
    scan_result=Column(Text)
    record_time=Column(Integer)

    def __init__(self, target, target_id, scan_result=""):
        self.target = target
        self.target_id = target_id
        self.scan_result = scan_result
        self.record_time=int(datetime.datetime.now().timestamp())


