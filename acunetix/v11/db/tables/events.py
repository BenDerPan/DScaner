# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\tables\events.py
__author__ = 'sanyi'
from sqlalchemy import *
import datetime
from dateutil.tz import tzlocal
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import UUID as C_UUID
from sqlalchemy.dialects.postgresql import JSONB as TYPE_JSONB
from .tables import metadata
from .settings_provider import settings
from helpers.mailer.base_mailer import Mailer
events = dict()
events['account_created'] = dict(id=0)
events['account_details_modified'] = dict(id=1)
events['account_email_change_asked'] = dict(id=2, email_template=dict(subject='Email change asked', subject_template=None, html_template='email_change_asked.html.jinja2', txt_template='email_change_asked.txt.jinja2'))
events['account_email_changed'] = dict(id=3)
events['account_password_reset_asked'] = dict(id=4, email_template=dict(subject='Password reset asked', subject_template=None, html_template='password_reset_asked.html.jinja2', txt_template='password_reset_asked.txt.jinja2'))
events['account_password_reset'] = dict(id=5)
events['account_password_changed'] = dict(id=6)
events['account_account_verified'] = dict(id=7)
events['account_login'] = dict(id=8)
events['account_logout'] = dict(id=9)
events['child_account_created'] = dict(id=100)
events['child_account_deleted'] = dict(id=101)
events['child_account_modified'] = dict(id=102)
events['child_account_set_access'] = dict(id=103)
events['target_created'] = dict(id=200)
events['target_modified'] = dict(id=201)
events['target_deleted'] = dict(id=202)
events['target_add_allowed_host'] = dict(id=203)
events['target_remove_allowed_host'] = dict(id=204)
events['target_not_responsive'] = dict(id=205)
events['target_validated'] = dict(id=206)
events['target_verification_succeeded'] = dict(id=207)
events['target_verification_failed'] = dict(id=208)
events['target_continuous_mode_disabled'] = dict(id=209, notification=True, email_template=dict(subject=None, subject_template='continuous_mode_disabled_subject.txt.jinja2', html_template='continuous_mode_disabled.html.jinja2', txt_template='continuous_mode_disabled.txt.jinja2'))
events['group_created'] = dict(id=300)
events['group_deleted'] = dict(id=301)
events['group_modified'] = dict(id=302)
events['group_targets_modified'] = dict(id=303)
events['scan_scheduled'] = dict(id=400)
events['scan_modified'] = dict(id=401)
events['scan_deleted'] = dict(id=402)
events['scan_started'] = dict(id=403)
events['scan_done'] = dict(id=404, notification=True, email_template=dict(subject=None, subject_template='scan_done_subject.txt.jinja2', html_template='scan_done.html.jinja2', txt_template='scan_done.txt.jinja2'))
events['scan_failed'] = dict(id=405, notification=True, severity=2, email_template=dict(subject=None, subject_template='scan_failed_subject.txt.jinja2', html_template='scan_failed.html.jinja2', txt_template='scan_failed.txt.jinja2'))
events['scan_mi_required_no_ui_session'] = dict(id=406, notifiction=True, severity=2)
events['scan_mi_required_scheduled_scan'] = dict(id=407, notifiction=True, severity=1)
events['scan_user_aborted'] = dict(id=406)
events['scan_job_starting'] = dict(id=410)
events['scan_job_done'] = dict(id=411)
events['scan_job_failed'] = dict(id=412)
events['scan_job_aborted'] = dict(id=413)
events['scan_scanner_event'] = dict(id=420)
events['scan_wvs_crawl_memlimit'] = dict(id=430, notification=True)
events['scan_wvs_aborted'] = dict(id=431, notification=True)
events['scan_wvs_sensor_found'] = dict(id=432)
events['scan_wvs_sensor_not_found'] = dict(id=433)
events['scan_wvs_ls_error'] = dict(id=434)
events['scan_wvs_au_error'] = dict(id=435)
events['scan_wvs_al_error'] = dict(id=436)
events['scan_wvs_crawling'] = dict(id=437)
events['scan_wvs_deep_scan'] = dict(id=438)
events['scan_wvs_scan_started'] = dict(id=439)
events['scan_wvs_scan_finished'] = dict(id=440)
events['scan_wvs_manual_browsing'] = dict(id=441)
events['scan_wvs_scan_resumed'] = dict(id=442)
events['vulnerability_marked_as'] = dict(id=500)
events['vulnerability_rediscovered'] = dict(id=501)
events['new_acumonitor_vulnerability'] = dict(id=502, notification=True)
events['report_asked'] = dict(id=600)
events['report_created'] = dict(id=601, notification=True, email_template=dict(subject=None, subject_template='report_done_subject.txt.jinja2', html_template='report_done.html.jinja2', txt_template='report_done.txt.jinja2'))
events['export_asked'] = dict(id=602)
events['export_created'] = dict(id=603)
events['report_failed'] = dict(id=604, severity=2, notification=True)
events['export_failed'] = dict(id=605, severity=2, notification=True)
events['wvs_new_version'] = dict(id=700, notification=True)

def get_event_severity(name):
    return events[name].get('severity', 0)


def create_event(name, owner_id, user_id=None, data=None, resource_type=None, resource_id=None, severity=None, shard=None, inhibit_notification=False):
    event_descriptor = events[name]
    if user_id is not None and user_id == owner_id:
        user_id = None
    if resource_id is not None and isinstance(resource_id, int):
        resource_id = '%032x' % (resource_id,)
    if inhibit_notification:
        consumed = None
    else:
        consumed = False if event_descriptor.get('notification') else None
    event = dict(owner_id=owner_id, user_id=user_id, type_id=events[name]['id'], data=data, severity=severity if severity is not None else event_descriptor.get('severity', 0), resource_type=resource_type, resource_id=resource_id, consumed=consumed)
    email_template = event_descriptor.get('email_template')
    if email_template:
        mailer = settings.get('mailer_object')
        if mailer:
            mailer.enqueue(dict(owner_id=owner_id, user_id=user_id, template=email_template, type=event_descriptor.get('type'), shard=shard, frontend_api_url=settings.get('frontend_url'), date_time=datetime.datetime.now(tz=tzlocal()), data=dict(event_name=name, event_data=data, severity=event['severity'], resource_type=resource_type, resource_id=resource_id)))
    return EventsTable.insert().values(event)


class EventResources:
    user = 1
    child_user = 2
    target = 3
    group = 4
    scan = 5
    scan_session = 6
    report = 7
    worker = 8
    vulnerability = 9
    export = 10


EventsTable = Table('events', metadata, Column('event_id', BIGINT, primary_key=True), Column('owner_id', C_UUID, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True), Column('user_id', C_UUID, ForeignKey('users.user_id', ondelete='SET NULL'), index=True), Column('type_id', INTEGER, index=True), Column('severity', INTEGER, default=0), Column('created', DateTime(true), default='now()'), Column('resource_type', INTEGER, index=True), Column('resource_id', TEXT, index=True), Column('data', TYPE_JSONB), Column('consumed', BOOLEAN, index=True))

class EventRow(object):
    event_id = None
    owner_id = None
    user_id = None
    creator_id = None
    type_id = None
    consumed = None
    resource_type = None
    resource_id = None
    severity = None

    def __str__(self):
        return 'R_event[%s]' % (self.event_id,)

    def __repr__(self):
        return self.__str__()


mapper(EventRow, EventsTable)