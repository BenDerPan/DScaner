# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\target2group.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
Target2GroupTable = Table('target2group', metadata, Column('target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), primary_key=True), Column('group_id', C_UUID, ForeignKey('groups.group_id', ondelete='CASCADE'), primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), index=True), Column('created', DateTime(true), default='now()'))

class Target2GroupRow(object):
    target_id = None
    group_id = None
    owner_id = None

    def __str__(self):
        return 'R_target2group[%s:%s]' % (self.target_id, self.group_id)

    def __repr__(self):
        return self.__str__()


mapper(Target2GroupRow, Target2GroupTable)