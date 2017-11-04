# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\vuln_types.py
__author__ = 'sanyi'
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import ARRAY as C_ARRAY
from .tables import metadata
sensor_details_template = '{{#file}}<p>Source file: <strong class="bb-dark">{{file}}</strong> line: <strong class="bb-dark">{{line}}</strong></p>{{/file}}\n{{#additional}}\n<p>Additional details:</p>\n<code><pre>{{additional}}</pre></code>\n{{/additional}}'
VulnTypesTable = Table('vuln_types', metadata, Column('vt_id', C_UUID, primary_key=True), Column('app_id', TEXT, index=True, unique=True), Column('name', TEXT, nullable=False, index=True), Column('severity', Integer, nullable=False, index=True), Column('details_template', TEXT), Column('impact', TEXT), Column('description', TEXT), Column('recommendation', TEXT), Column('long_description', TEXT), Column('tags', C_ARRAY(TEXT), index=True), Column('cvss2', TEXT, index=True), Column('cvss3', TEXT, index=True), Column('cvss_score', REAL, index=True), Column('refs', C_ARRAY(TEXT)))

class VulnTypeRow(object):
    vt_id = None
    name = None
    severity = None
    tags = None
    cvss2 = None
    cvss3 = None
    cvss_score = None
    impact = None
    description = None
    recommendation = None
    long_description = None
    refs = None
    details_template = None
    app_id = None

    def __str__(self):
        return 'R_vuln_type[%s]=%s' % (self.vt_id, self.name)

    def __repr__(self):
        return self.__str__()


mapper(VulnTypeRow, VulnTypesTable)