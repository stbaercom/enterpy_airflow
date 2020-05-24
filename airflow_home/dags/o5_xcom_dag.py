import json
from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

dag = DAG('o5_xcom_dag',
          description='Simple XCOM Operation',
          start_date=datetime(2020, 1, 1),
          schedule_interval="@daily")

def setter():
    return {"key": "value", "list": [1, 2, 3, 4]}

def getter(**context):
    ti = context['task_instance']
    value = ti.xcom_pull(key=None, task_ids='set_op')
    fp = "/Users/imhiro/Desktop/conferences_2020/4_enterpy/enterpy_2/code/data/xcom.txt"
    with open(fp, mode="w") as out:
        json.dump(value,out)

set_op = PythonOperator(
    task_id='test_op', provide_context=True,
    python_callable=setter, dag=dag)

get_op = PythonOperator(
    task_id='action_op', provide_context=True,
    python_callable=getter, dag=dag)

set_op >> get_op
