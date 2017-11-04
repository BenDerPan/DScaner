# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\report_templates.py
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from db.tables import metadata
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
ReportTemplatesTable = Table('report_templates', metadata, Column('report_template_id', C_UUID, primary_key=True), Column('name', TEXT, nullable=False), Column('data', TYPE_JSONB), Column('sort_order', INTEGER), Column('type', INTEGER))

class ReportType:
    report = 0
    export = 1


class ReportTemplateRow(object):
    report_template_id = None
    name = None
    sort_order = None
    data = None
    type = None

    def __str__(self):
        return 'R_report_template[%s]=%s' % (self.report_template_id, self.name)

    def __repr__(self):
        return self.__str__()


mapper(ReportTemplateRow, ReportTemplatesTable)