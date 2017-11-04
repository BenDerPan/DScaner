# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\targets.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from .tables import metadata
TargetsTable = Table('targets', metadata, Column('target_id', C_UUID, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), index=True), Column('address', TEXT, nullable=False, index=True), Column('description', TEXT, nullable=False, default=''), Column('criticality', INTEGER, default=10), Column('created', DateTime(true), default='now()'), Column('modified', DateTime(true)), Column('last_scan_session_id', C_UUID(ForeignKey('scans_sessions.scan_session_id', ondelete='SET NULL'))), Column('last_scan_id', C_UUID(ForeignKey('scans.scan_id', ondelete='SET NULL'))), Column('deleted_at', DateTime(true)), Column('manual_intervention', BOOLEAN))
Index('ix_targets_not_deleted', TargetsTable.c.deleted_at, postgresql_where=TargetsTable.c.deleted_at.is_(None))

class TargetRow(object):
    target_id = None
    owner_id = None
    description = None
    address = None
    criticality = None
    deleted_at = None
    last_scan_session_id = None
    manual_intervention = None

    def __str__(self):
        return 'R_target[%s:%s]=%s' % (self.target_id, self.owner_id, self.address)

    def __repr__(self):
        return self.__str__()


mapper(TargetRow, TargetsTable)