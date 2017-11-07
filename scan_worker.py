from celery import Celery
import datetime
import time
import json
from config import *
from acunetix.awvs import *
from acunetix.v11.db.db_helper import DBHelper


def make_scan_result(target, target_id, scan_result, error=0, error_msg="OK"):
    result = {}
    result['error'] = error
    result['error_msg'] = error_msg
    result['target'] = target
    result['target_id'] = target_id
    result['result'] = scan_result
    result['record_time'] = datetime.datetime.now().timestamp()
    return json.dumps(result)


awvsScaner = AwvsScaner()


dbHelper = DBHelper()


def add_target(url, description=None, criticality=10):
    target = dbHelper.get_target(url)
    if target:
        return target.target_id
    return awvsScaner.v11.add_target(url=url, description=description, criticality=criticality)

app = Celery(CELERY_TASK_NAME, broker=CELERY_BROKER, backend=CELERY_BACKEND)
@app.task
def scan(target, level=awvsScaner.v11.PROFILE_ID_HIGH_RISK_VULNERABILITIES):
    print("[*]接收到扫描任务:{0}".format(target))
    target_id = add_target(target,description=target,criticality=10)
    if not target_id:
        result = make_scan_result(target, target_id, "", 1, "Add target failed.")
        return result
    targets,targets_full = awvsScaner.v11.get_running_targets(target_id=target_id)
    canStart=False
    if target not in targets:
        canStart=True
    else:
        if ("completed" in targets[target] or "failed" in targets[target] or "aborting" in targets[target] or "aborted" in targets[target]) \
                and ("running" not in targets[target] and "queued" not in targets[target] and "processing" not in targets[target]):
            canStart=True
    if canStart:
        target_id = awvsScaner.v11.start_scan_by_target_id(target_id=target_id, profile_id=level)
        if not target_id:
            result = make_scan_result(target, target_id, "", 1, "Start scan failed.")
            return result
    _, target_full_new = awvsScaner.v11.get_running_targets(target_id)
    time_scan_id={}
    for t in target_full_new:
        time_scan_id[t['start_time']]=t['scan_id']
    max_time=max(time_scan_id.keys())
    scan_id=time_scan_id[max_time]
    while True:
        status=awvsScaner.v11.get_scan_status(scan_id)
        print("[*]Checking [{0}] Running Status:{1}".format(target,status))
        if status.lower() in ["completed","failed","aborted"]:
            vulns = dbHelper.get_target_vuln_with_details(target_id)
            result = make_scan_result(target, target_id, vulns)
            return result
        time.sleep(15)


if __name__ == '__main__':
    target="http://testphp.vulnweb.com"
    target_id="b306e7a0-9da2-4961-af94-495f8e7d0619"
    scan("http://testphp.vulnweb.com")
