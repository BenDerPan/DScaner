# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\uploads.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy import not_ as sql_not
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
UploadsTable = Table('uploads', metadata, Column('upload_id', C_UUID, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), index=True), Column('unique_id', C_UUID), Column('expires', DateTime(True)), Column('created', DateTime(True), default='now()'), Column('current_size', INTEGER, default=0), Column('size', INTEGER), Column('name', TEXT), Column('resource_id', C_UUID), Column('deleted_at', DateTime(True)), Column('status', BOOLEAN, default=False), Column('actions', TYPE_JSONB), Column('data', TYPE_JSONB))
Index('ix_uploads_not_deleted', UploadsTable.c.deleted_at, postgresql_where=UploadsTable.c.deleted_at.is_(None))
Index('ix_uploads_unique_id', UploadsTable.c.unique_id, unique=True, postgresql_where=sql_not(UploadsTable.c.deleted_at.is_(None)))

class UploadRow(object):
    upload_id = None
    owner_id = None
    creator_id = None
    expires = None
    deleted_at = None
    status = None
    current_size = None
    size = None
    data = None

    def __str__(self):
        return 'R_upload[%s:%s]' % (self.owner_id, self.upload_id)

    def __repr__(self):
        return self.__str__()


mapper(UploadRow, UploadsTable)