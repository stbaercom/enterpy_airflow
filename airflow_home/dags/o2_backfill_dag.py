import json
import os
from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import requests



dag = DAG('02_backfill_dag',
          description='Python Operator with Backfill',
          start_date=datetime(2020, 1, 1),
          schedule_interval="@daily",)

def backfill(*args, **kwargs):
    p = "/Users/imhiro/Desktop/conferences_2020/4_enterpy/enterpy_2/code/data"
    date = kwargs['ds']
    url = f"http://localhost:5000/daily/{date}"

    res = requests.get(url)
    if res.ok:
        j = res.json()
        with open(os.path.join(p,f"res_{date}.json"),mode="w") as out:
            json.dump(j,out)
    else:
        raise Exception(f"Error {res.status_code}")

backfill_op = PythonOperator(
    task_id='backfill_task',
    provide_context=True,
    python_callable=backfill,
    dag=dag)

backfill_op

