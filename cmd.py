from tasks import scan
import time
results=[]
for i in range(10):
    result=scan.delay(i)
    results.append(result)

while True:
    readyCount=0
    for r in results:
        if r.ready():
            readyCount+=1
            print(r.get())
            time.sleep(1)
    if readyCount==len(results):
        break
