# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\user2shard.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
User2ShardTable = Table('user2shard', metadata, Column('user_id', C_UUID, primary_key=True), Column('email', TEXT, unique=True, nullable=False), Column('shard', TEXT), Column('status', Integer))

class User2ShardRow(object):
    STATUS_LOGIN_DISABLED = 0
    STATUS_LOGIN_ENABLED = 1
    user_id = None
    email = None
    status = 0

    def __str__(self):
        return 'R_user2_shard[%s]=%s' % (self.user_id, self.email)

    def __repr__(self):
        return self.__str__()


mapper(User2ShardRow, User2ShardTable)