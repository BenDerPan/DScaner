# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\scans.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from .tables import metadata
ScansTable = Table('scans', metadata, Column('scan_id', C_UUID, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=true), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), index=true), Column('current_session_id', C_UUID, ForeignKey('scan_sessions.scan_session_id', ondelete='SET NULL')), Column('previous_session_id', C_UUID, ForeignKey('scan_sessions.scan_session_id', ondelete='SET NULL')), Column('created', DateTime(true), default='now()'), Column('target_id', C_UUID, ForeignKey('targets.target_id', ondelete='CASCADE'), nullable=False, index=true), Column('profile_id', C_UUID, ForeignKey('scanning_profiles.profile_id', ondelete='RESTRICT'), nullable=False), Column('recurrence', TEXT), Column('schedule_disabled', BOOLEAN, default=False), Column('schedule_start_date', DateTime(true), index=True), Column('next_run', DateTime(True), index=True), Column('history_limit', INTEGER), Column('deleted_at', DateTime(true)), Column('report_template_id', C_UUID, ForeignKey('report_templates.report_template_id', ondelete='SET NULL')), Column('continuous', BOOLEAN, default=False), Column('schedule_time_sensitive', BOOLEAN, default=False))
Index('ix_scans_not_deleted', ScansTable.c.deleted_at, postgresql_where=ScansTable.c.deleted_at.is_(None))

class ScanRow(object):
    owner_id = None
    schedule_id = None
    target_id = None
    scan_id = None
    deleted_at = None
    next_run = None
    schedule_disabled = None
    recurrence = None
    profile_id = None
    current_session_id = None
    creator_id = None
    report_template_id = None
    continuous = None
    schedule_start_date = None

    def __str__(self):
        return 'R_scan[%s:%s]' % (self.scan_id, self.owner_id)

    def __repr__(self):
        return self.__str__()


mapper(ScanRow, ScansTable)