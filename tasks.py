from celery import Celery
import time
app=Celery("tasks",broker="redis://localhost:6379/0",backend="redis://localhost:6379/1")

@app.task
def scan(target):
    print("正在扫描{}".format(target))
    time.sleep(10)
    print("任务{}扫描完成".format(target))
    return "Task={0} Result=结果结果结果哦".format(target)

