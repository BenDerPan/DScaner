# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\groups.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
GroupsTable = Table('groups', metadata, Column('group_id', C_UUID, primary_key=True), Column('name', TEXT), Column('description', TEXT), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False, index=True), Column('created', DateTime(true), default='now()'))
Index('ix_groups_unique_name', GroupsTable.c.owner_id, GroupsTable.c.name, unique=True)

class GroupRow(object):
    group_id = None
    owner_id = None
    name = None

    def __str__(self):
        return 'R_group[%s:%s]=%s' % (self.owner_id, self.group_id, self.name)

    def __repr__(self):
        return self.__str__()


mapper(GroupRow, GroupsTable)