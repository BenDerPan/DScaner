# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\issue_trackers.py
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from db.tables import metadata
IssueTrackersTable = Table('issue_trackers', metadata, Column('issue_tracker_id', C_UUID, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=true), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), index=true), Column('name', TEXT, nullable=False), Column('data', TYPE_JSONB, nullable=False), Column('deleted_at', DateTime(true)))

class IssueTrackerRow(object):
    issue_tracker_id = None
    name = None
    data = None
    owner_id = None
    deleted_at = None

    def __init__(self, issue_tracker_id):
        self.issue_tracker_id = issue_tracker_id

    def __str__(self):
        return 'R_IssueTracker[%s:%s]' % (self.issue_tracker_id, self.name)

    def __repr__(self):
        return self.__str__()


mapper(IssueTrackerRow, IssueTrackersTable)