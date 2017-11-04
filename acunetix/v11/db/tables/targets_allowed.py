# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\targets_allowed.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
TargetsAllowedTable = Table('targets_allowed', metadata, Column('target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), primary_key=True), Column('allowed_target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), primary_key=True))

class TargetsAllowedRow(object):
    target_id = None
    allowed_target_id = None

    def __str__(self):
        return 'R_targets_allowed %s=%s' % (self.target_id, self.allowed_target_id)

    def __repr__(self):
        return self.__str__()


mapper(TargetsAllowedRow, TargetsAllowedTable)