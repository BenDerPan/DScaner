# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\targets_configurations.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from .tables import metadata
TargetConfigurationTable = Table('target_configuration', metadata, Column('target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), primary_key=True), Column('name', TEXT, primary_key=True), Column('value', TYPE_JSONB))

class TargetConfigurationRow(object):
    target_id = None
    name = None
    value = None

    def __str__(self):
        return 'R_target_settings[%s:%s]=%s' % (self.target_id, self.name, self.value)

    def __repr__(self):
        return self.__str__()


mapper(TargetConfigurationRow, TargetConfigurationTable)