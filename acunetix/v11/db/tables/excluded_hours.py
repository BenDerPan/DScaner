# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\excluded_hours.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from db.tables import metadata
ExcludedHoursTable = Table('excluded_hours', metadata, Column('excluded_hours_id', C_UUID, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), index=True), Column('name', TEXT), Column('data', TYPE_JSONB), Column('time_offset', INTEGER, default=0), Column('created', DateTime(true), default='now()'), Column('deleted_at', DateTime(true)))
Index('ix_excluded_hours_unique_name', ExcludedHoursTable.c.owner_id, ExcludedHoursTable.c.name, unique=True)

class ExcludedHoursRow(object):
    owner_id = None
    excluded_hours_id = None
    name = None
    deleted_at = None
    time_offset = None
    data = None

    def __str__(self):
        return 'R_excluded_hours[%s]=%s' % (self.owner_id, self.name)

    def __repr__(self):
        return self.__str__()


mapper(ExcludedHoursRow, ExcludedHoursTable)