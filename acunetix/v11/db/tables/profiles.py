# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\profiles.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
ProfilesTable = Table('scanning_profiles', metadata, Column('profile_id', C_UUID, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), index=true), Column('creator_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), index=true), Column('name', TEXT, nullable=False), Column('jobs', TYPE_JSONB), Column('sort_order', INTEGER), Column('deleted_at', DateTime(true)))

class ProfileRow(object):
    profile_id = None
    owner_id = None
    creator_id = None
    name = None
    sort_order = None
    jobs = None
    deleted_at = None

    def __str__(self):
        return 'R_profile[%s]=%s' % (self.profile_id, self.name)

    def __repr__(self):
        return self.__str__()


mapper(ProfileRow, ProfilesTable)