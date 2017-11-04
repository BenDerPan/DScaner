# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\licenses.py
from sqlalchemy import *
from sqlalchemy.orm import mapper
from db.tables import metadata
LicensesTable = Table('licenses', metadata, Column('license_key', TEXT, primary_key=True))

class LicenseRow(object):
    license_key = None

    def __init__(self, license_key):
        self.license_key = license_key

    def __str__(self):
        return 'R_license[%s]' % (self.license_key,)

    def __repr__(self):
        return self.__str__()


mapper(LicenseRow, LicensesTable)