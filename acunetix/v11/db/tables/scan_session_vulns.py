# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\scan_session_vulns.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import ARRAY as C_ARRAY
from .target_vulns import DetailsType
from .functions import sql_id_generator
from .tables import metadata
ScanSessionVulnsTable = Table('scan_session_vulns', metadata, Column('vuln_id', BIGINT, primary_key=True, default=sql_id_generator()), Column('scan_session_id', C_UUID, ForeignKey('scan_sessions.scan_session_id', ondelete='CASCADE'), nullable=False, index=True), Column('vt_id', C_UUID, ForeignKey('vuln_types.vt_id', ondelete='CASCADE'), index=True, nullable=False), Column('loc_id', INTEGER, nullable=False, index=True), Column('loc_detail', TEXT, nullable=False, index=True), Column('vuln_hash', C_UUID, nullable=False), Column('details', TEXT), Column('details_type', DetailsType, default='text'), Column('sensor_details', TEXT), Column('tags', C_ARRAY(TEXT), index=True), Column('request', TEXT), Column('source', TEXT), Column('request_secure', BOOLEAN), Column('request_port', INTEGER), Column('use_ssl', BOOLEAN), Column('attack_vector', TEXT), ForeignKeyConstraint(['scan_session_id', 'loc_id'], [
 'locations.scan_session_id', 'locations.loc_id'], ondelete='CASCADE'), Column('deleted_at', DateTime(true)))
Index('ix_scan_session_vulns_not_deleted', ScanSessionVulnsTable.c.deleted_at, postgresql_where=ScanSessionVulnsTable.c.deleted_at.is_(None))
Index('ix_scan_session_vulns_unique_hash', ScanSessionVulnsTable.c.scan_session_id, ScanSessionVulnsTable.c.vuln_hash, unique=True)

class ScanSessionVulnRow(object):
    vuln_id = None
    scan_session_id = None
    vt_id = None
    tags = None
    loc_detail = None
    loc_id = None
    request = None
    details = None
    details_type = None
    vuln_hash = None
    source = None
    sensor_details = None

    def __str__(self):
        return 'R_vuln:%s' % (self.vuln_id,)

    def __repr__(self):
        return self.__str__()


mapper(ScanSessionVulnRow, ScanSessionVulnsTable)