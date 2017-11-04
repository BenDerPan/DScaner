# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\target_vulns_stats.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from .tables import metadata
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import ARRAY as C_ARRAY
TargetVulnsStatsTable = Table('target_vulns_stats', metadata, Column('target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), primary_key=True), Column('vuln_stats', C_ARRAY(INTEGER)))

class TargetVulnsStatsRow(object):
    target_id = None
    vuln_stats = None

    def __str__(self):
        return 'R_target_vulns_stats:%s' % (self.target_id,)

    def __repr__(self):
        return self.__str__()


mapper(TargetVulnsStatsRow, TargetVulnsStatsTable)