# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\locations.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import ARRAY as C_ARRAY
from sqlalchemy.types import TypeDecorator
from db.tables import metadata

class LocationType(TypeDecorator):
    impl = INTEGER
    loc_type_str_2_int = dict(file=0, folder=1)
    loc_type_int_to_str = dict(zip(loc_type_str_2_int.values(), loc_type_str_2_int.keys()))

    def process_bind_param(self, value, dialect):
        return self.loc_type_str_2_int.get(value)

    def process_result_value(self, value, dialect):
        return self.loc_type_int_to_str.get(value)

    def python_type(self):
        return str

    def process_literal_param(self, value, dialect):
        pass


loc_type_str_to_int = dict(file=0, folder=1)
LocationsTable = Table('locations', metadata, Column('loc_id', INTEGER, nullable=False, primary_key=True), Column('scan_session_id', C_UUID, ForeignKey('scan_sessions.scan_session_id', ondelete='CASCADE'), nullable=False, primary_key=True, index=True), Column('name', TEXT, nullable=False), Column('parent_id', INTEGER, index=True), Column('source_id', INTEGER, index=True), Column('root_id', INTEGER, index=True), Column('tags', C_ARRAY(TEXT), index=True), Column('path', TEXT), Column('loc_type', LocationType), Column('input_data', TEXT), ForeignKeyConstraint(['scan_session_id', 'parent_id'], [
 'locations.scan_session_id', 'locations.loc_id'], ondelete='CASCADE'))

class LocationRow(object):
    loc_id = None
    parent_id = None
    scan_session_id = None
    tags = None
    root_id = None
    path = None
    loc_type = None
    name = None
    source_id = None
    input_data = None

    def __str__(self):
        return 'R_location:%s:%s' % (self.scan_session_id, self.loc_id)

    def __repr__(self):
        return self.__str__()


mapper(LocationRow, LocationsTable)