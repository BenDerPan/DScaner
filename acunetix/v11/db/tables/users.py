# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\users.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy import not_ as sqlachemy_not
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as TYPE_UUID
from sqlalchemy.dialects.postgresql import ENUM as TYPE_ENUM
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from db.tables import metadata
UserRoles = TYPE_ENUM('none', 'master', 'tech_admin', 'tester', 'auditor', name='user_roles', metadata=metadata)
LicenseTypes = TYPE_ENUM('trial', 'customer', 'demo', name='license_types', metadata=metadata)
UsersTable = Table('users', metadata, Column('user_id', TYPE_UUID, primary_key=True), Column('email', TEXT, nullable=False), Column('password', TEXT), Column('confirmed', Boolean, default=False), Column('first_name', TEXT), Column('last_name', TEXT), Column('phone', TEXT), Column('country', TEXT), Column('website', TEXT), Column('company', TEXT), Column('owner_id', TYPE_UUID, ForeignKey('users.user_id', ondelete='CASCADE')), Column('license_key', TEXT, ForeignKey('licenses.license_key', ondelete='RESTRICT')), Column('api_key', TEXT, unique=True), Column('access_all_groups', Boolean, default=False), Column('role', UserRoles, default='none'), Column('notifications', TYPE_JSONB, default=dict()), Column('enabled', Boolean, default=True), Column('verified_by_authority', Boolean), Column('created', DateTime(true), default='now()'), Column('modified', DateTime(true), default='now()'), Column('deleted_at', DateTime(true)), Column('license_type', LicenseTypes), Column('license_ends', INTEGER))
Index('ix_users_not_deleted', UsersTable.c.deleted_at, postgresql_where=UsersTable.c.deleted_at.is_(None))
Index('ix_users_unique_active_email', UsersTable.c.email, unique=True, postgresql_where=UsersTable.c.deleted_at.is_(None))

class UserRow(object):
    user_id = None
    owner_id = None
    email = None
    password = None
    license_key = None
    api_key = None
    enabled = None
    access_all_groups = None
    deleted_at = None
    first_name = None
    last_name = None
    notifications = None

    def __str__(self):
        return 'R_user[%s:%s]=%s' % (self.user_id, self.owner_id, self.email)

    def __repr__(self):
        return self.__str__()


mapper(UserRow, UsersTable)