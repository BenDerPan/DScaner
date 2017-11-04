from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# from acunetix.v11.db.tables.targets import *

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper
Base = declarative_base()

metadata = MetaData()

lessnet = Table('lessnet', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )

class LessNet(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(LessNet, lessnet)

engine = create_engine('postgresql+psycopg2://wvs:wvs@192.168.4.8:35432/wvs')
print('OK')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

ll = LessNet(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ll)
session.commit()

for instance in session.query(LessNet).order_by(LessNet.id):
    print(instance.name, instance.fullname)
