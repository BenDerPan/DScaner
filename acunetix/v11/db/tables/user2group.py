# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\user2group.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
User2GroupTable = Table('user2group', metadata, Column('user_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, primary_key=True), Column('group_id', C_UUID, ForeignKey('groups.group_id', ondelete='CASCADE'), nullable=False, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), index=True), Column('created', DateTime(true), default='now()'))

class User2GroupRow(object):
    group_id = None
    user_id = None
    owner_id = None

    def __str__(self):
        return 'R_user_access[%s:%s]' % (self.user_id, self.group_id)

    def __repr__(self):
        return self.__str__()


mapper(User2GroupRow, User2GroupTable)