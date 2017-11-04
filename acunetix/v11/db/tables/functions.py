# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118]
# Embedded file name: db\functions.py
from db import FunctionWrapper

def sql_locations_add_tag(scan_session_id, loc_id, tag):
    return FunctionWrapper('locations_add_tag', scan_session_id=scan_session_id, loc_id=loc_id, tag=tag)


def sql_id_generator():
    return FunctionWrapper('id_generator')