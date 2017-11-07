from scan_worker import scan
import time
import json
from storage.storage_manager import StorageManager
from push import RestApiPusher
from config import *
from storage.tables.vuln_task import VulnTask

storageManager = StorageManager()
storageManager.init_db()


def get_all_targets():
    targets = ["http://testhtml5.vulnweb.com",
               "http://testphp.vulnweb.com",
               "http://testasp.vulnweb.com/",
               "http://testaspnet.vulnweb.com/"
               ]
    return targets

RestApiPusher.PUSH_URL = VULN_PUSH_API_URL
while True:
    targets = get_all_targets()
    results = []
    for target in targets:
        result = scan.delay(target)
        results.append(result)

    while True:
        for i in range(len(results) - 1, -1, -1):
            if results[i].ready():
                r = results[i].get()
                r=json.loads(r)
                print(r)
                try:
                    vulnTask = VulnTask(r['target'],r['target_id'], r)
                    storageManager.Session.add(vulnTask)
                    storageManager.save()
                    if ENABLE_VULN_PUSH:
                        res = RestApiPusher.push(r)
                    results.pop(i)
                except Exception as e:
                    print("[!]处理任务结果异常:{0}".format(e))
        if len(results) < 1:
            break
        time.sleep(5)
