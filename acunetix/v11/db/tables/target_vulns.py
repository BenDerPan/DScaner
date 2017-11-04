# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\target_vulns.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from .tables import metadata
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import ARRAY as C_ARRAY
from sqlalchemy.dialects.postgresql import ENUM as TYPE_ENUM
from .functions import sql_id_generator
DetailsType = TYPE_ENUM('text', 'data', 'json', name='vuln_details_type', metadata=metadata)
VulnStatus = TYPE_ENUM('open', 'fixed', 'ignored', 'false_positive', name='vulnerability_status', metadata=metadata)
TargetVulnsTable = Table('target_vulns', metadata, Column('vuln_id', BIGINT, primary_key=True, default=sql_id_generator()), Column('target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), nullable=False, index=True), Column('scan_session_id', C_UUID, ForeignKey('scan_sessions.scan_session_id', ondelete='SET NULL'), index=True), Column('vt_id', C_UUID, ForeignKey('vuln_types.vt_id', ondelete='RESTRICT'), index=True, nullable=False), Column('url', TEXT, nullable=False), Column('loc_detail', TEXT, nullable=False, index=True), Column('vuln_hash', C_UUID, nullable=False, index=True), Column('details', TEXT), Column('details_type', DetailsType, default='text'), Column('sensor_details', TEXT), Column('first_seen', DateTime(true), default='now()'), Column('last_seen', DateTime(true), default='now()'), Column('fixed_at', DateTime(true)), Column('tags', C_ARRAY(TEXT), index=True), Column('request', TEXT), Column('source', TEXT), Column('status', VulnStatus, default='open'), Column('criticality', INTEGER, default=0), Column('rediscovered', Boolean, default=False), Column('deleted_at', DateTime(true)), Column('severity', INTEGER), Column('name', TEXT), Column('request_secure', BOOLEAN), Column('request_port', INTEGER), Column('use_ssl', BOOLEAN), Column('attack_vector', TEXT), Column('continuous', BOOLEAN, default=False), Column('issue_id', TEXT), Column('issue_tracker_id', C_UUID, ForeignKey('issue_trackers.issue_tracker_id', ondelete='RESTRICT'), index=True))
Index('ix_target_vulns_default_sorting', TargetVulnsTable.c.criticality, TargetVulnsTable.c.severity, TargetVulnsTable.c.name, TargetVulnsTable.c.vuln_id)
Index('ix_target_vulns_hash', TargetVulnsTable.c.target_id, TargetVulnsTable.c.vuln_hash, unique=True)
Index('ix_target_vulns_not_deleted', TargetVulnsTable.c.deleted_at, postgresql_where=TargetVulnsTable.c.deleted_at.is_(None))

class TargetVulnRow(object):
    vuln_id = None
    last_seen = None
    first_seen = None
    target_id = None
    vuln_hash = None
    status = None
    vt_id = None
    rediscovered = None
    tags = None
    loc_detail = None
    url = None
    criticality = None
    request = None
    details = None
    details_type = None
    severity = None
    name = None
    scan_session_id = None
    source = None
    continuous = None
    issue_id = None
    issue_tracker_id = None
    sensor_details = None

    def __str__(self):
        return 'R_target_vuln:%s' % (self.vuln_id,)

    def __repr__(self):
        return self.__str__()


mapper(TargetVulnRow, TargetVulnsTable)