from celery import Celery
from config import *
from acunetix.awvs import *
from acunetix.v11.db.db_helper import DBHelper
awvsScaner=AwvsScaner()

app=Celery(CELERY_TASK_NAME,broker=CELERY_BROKER,backend=CELERY_BACKEND)
dbHelper=DBHelper()
@app.task
def scan(target):
    awvsScaner.v11.start_scan()

@app.task
def get_scan_results():
    pass




