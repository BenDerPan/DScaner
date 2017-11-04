# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\scan_sessions.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from sqlalchemy.dialects.postgresql import ENUM as TYPE_ENUM
from db.tables import metadata
ScanStatus = TYPE_ENUM('scheduled', 'queued', 'starting', 'processing', 'completed', 'aborting', 'aborted', 'failed', name='scan_status', metadata=metadata)
ScanSessionsTable = Table('scan_sessions', metadata, Column('scan_session_id', C_UUID, primary_key=True), Column('scan_id', C_UUID, ForeignKey('scans.scan_id', ondelete='CASCADE'), nullable=False), Column('target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), nullable=False, index=True), Column('created', DateTime(true), default='now()'), Column('status', ScanStatus, default='scheduled'), Column('progress', INTEGER, default=0), Column('scan_key', C_UUID), Column('start_date', DateTime(true)), Column('start_expected', DateTime(true)), Column('end_date', DateTime(true)), Column('allowed_targets', TYPE_JSONB), Column('information', TYPE_JSONB), Column('used_profile_id', C_UUID, ForeignKey('scanning_profiles.profile_id', ondelete='RESTRICT')), Column('deleted_at', DateTime(true)), Column('event_level', INTEGER))
Index('ix_scan_sessions_not_deleted', ScanSessionsTable.c.deleted_at, postgresql_where=ScanSessionsTable.c.deleted_at.is_(None))

class ScanSessionRow(object):
    scan_session_id = None
    scan_id = None
    target_id = None
    status = None
    start_expected = None
    start_date = None
    end_date = None
    deleted_at = None
    used_profile_id = None
    scan_key = None
    allowed_targets = None
    event_level = None
    progress = None

    def __str__(self):
        return 'R_scan_session[%s]' % (self.scan_session_id,)

    def __repr__(self):
        return self.__str__()


mapper(ScanSessionRow, ScanSessionsTable)