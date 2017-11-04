# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\system_config.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from db.tables import metadata
SystemConfigTable = Table('system_config', metadata, Column('name', TEXT, primary_key=True), Column('value', TYPE_JSONB))

class SystemConfigRow(object):
    name = None
    value = None

    def __str__(self):
        return 'R_system %s=%s' % (self.name, self.value)

    def __repr__(self):
        return self.__str__()


mapper(SystemConfigRow, SystemConfigTable)