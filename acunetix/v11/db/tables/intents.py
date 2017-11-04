# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\intents.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from db.tables import metadata
IntentsTable = Table('intents', metadata, Column('intent_id', C_UUID, primary_key=True), Column('unique_key', TEXT, unique=True), Column('expires', DateTime(true), index=True), Column('data', TYPE_JSONB), Column('created', DateTime(true), default='now()'), Column('status', INTEGER, default=0))

class IntentRow(object):
    intent_id = None
    unique_key = None
    expires = None
    data = None
    status = None

    def __str__(self):
        return 'R_intent[%s]' % (self.intent_id,)

    def __repr__(self):
        return self.__str__()


mapper(IntentRow, IntentsTable)