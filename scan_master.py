from scan_worker import scan
import time
from storage.storage_manager import StorageManager
from push import RestApiPusher
from config import *
storageManager=StorageManager()
storageManager.init_db()

def get_all_targets():
    targets=["http://testhtml5.vulnweb.com",
             "http://testphp.vulnweb.com",
             "http://testasp.vulnweb.com/",
             "http://testaspnet.vulnweb.com/"
             ]
    return targets


RestApiPusher.PUSH_URL=VULN_PUSH_API_URL
while True:
    targets=get_all_targets()
    results=[]
    for target in targets:
        result=scan.delay(target)
        results.append(result)
        break

    while True:
        for i  in range(len(results)-1,-1,-1):
            if results[i].ready():
                print(results[i].get())
                r=results[i].get()
                res=RestApiPusher.push(r)
                if res:
                    results.pop(i)
        if len(results)<1:
            break
        time.sleep(5)