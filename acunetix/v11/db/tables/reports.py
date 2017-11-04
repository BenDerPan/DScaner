# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\reports.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from .tables import metadata
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from sqlalchemy.dialects.postgresql import ENUM as TYPE_ENUM
ReportStatus = TYPE_ENUM('queued', 'processing', 'completed', 'failed', name='report_status', metadata=metadata)
ReportSourceType = TYPE_ENUM('all_vulnerabilities', 'targets', 'groups', 'scans', 'scan_result', 'vulnerabilities', 'scan_vulnerabilities', name='report_source_type', metadata=metadata)
ReportsTable = Table('reports', metadata, Column('report_id', C_UUID, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=true), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), index=true), Column('created', DateTime(true), default='now()', index=True), Column('report_template_id', C_UUID, ForeignKey('report_templates.report_template_id', ondelete='SET NULL')), Column('source', TYPE_JSONB), Column('source_type', ReportSourceType, index=True), Column('hash', TEXT), Column('result', TYPE_JSONB), Column('status', ReportStatus, default='queued'), Column('deleted_at', DateTime(true)))

class ReportRow(object):
    report_id = None
    deleted_at = None
    owner_id = None
    creator_id = None
    report_template_id = None
    status = None
    created = None
    source_type = None

    def __str__(self):
        return 'R_report %s' % (self.report_id,)

    def __repr__(self):
        return self.__str__()


mapper(ReportRow, ReportsTable)