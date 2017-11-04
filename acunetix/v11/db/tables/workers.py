# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\workers.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from sqlalchemy.dialects.postgresql import ENUM as TYPE_ENUM
from .tables  import metadata
WorkerStatus = TYPE_ENUM('promised', 'functional', 'shutdown_scheduled', 'offline', name='worker_status', metadata=metadata)
WorkersTable = Table('workers', metadata, Column('worker_id', TEXT, primary_key=True), Column('status', WorkerStatus, index=True), Column('scanning_app', TEXT, index=True, nullable=False), Column('address', TEXT), Column('port', INTEGER), Column('max_job_count', INTEGER, default=4), Column('worker_data', TYPE_JSONB), Column('created', DateTime(true), default='now()'), Column('start_date', DateTime(true)), Column('shutdown_date', DateTime(true)))

class WorkerRow(object):
    worker_id = None
    status = None
    scanning_app = None

    def __str__(self):
        return 'R_worker[%s:%s]' % (self.worker_id, self.scanning_app)

    def __repr__(self):
        return self.__str__()


mapper(WorkerRow, WorkersTable)