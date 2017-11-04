# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\scan_session_jobs.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from .scan_sessions import ScanStatus
from .tables import metadata
ScanSessionJobsTable = Table('scan_session_jobs', metadata, Column('scan_session_id', C_UUID, ForeignKey('scan_sessions.scan_session_id', ondelete='CASCADE'), nullable=False, primary_key=True), Column('scanning_app', TEXT, primary_key=True), Column('worker_id', C_UUID, index=True), Column('status', ScanStatus, index=True, nullable=False), Column('status_data', TYPE_JSONB), Column('result_processed', BOOLEAN, default=False), Column('abort_requested', BOOLEAN, default=False), Column('start_date', DateTime(true)), Column('end_date', DateTime(true)), Column('start_deadline', DateTime(true)), Column('end_deadline', DateTime(true)), Column('last_update', DateTime(true)), Column('acumonitor_id', INTEGER), Column('stats', TYPE_JSONB), Column('manual_processing_required', TYPE_JSONB))

class ScanSessionJobRow(object):
    scan_session_id = None
    scanning_app = None
    status = None
    result_processed = None
    last_update = None
    end_deadline = None
    abort_requested = None
    start_deadline = None
    acumonitor_id = None
    stats = None

    def __str__(self):
        return 'R_job[%s:%s]' % (self.scan_session_id, self.scanning_app)

    def __repr__(self):
        return self.__str__()


mapper(ScanSessionJobRow, ScanSessionJobsTable)