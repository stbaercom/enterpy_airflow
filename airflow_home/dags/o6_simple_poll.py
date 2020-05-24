import json
import random
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


from airflow.exceptions import AirflowSkipException
dag = DAG('o6_simple_poll',description='Simple XCOM Operation',
          start_date=datetime(2020, 1, 1),
          schedule_interval="@daily",
          )

def test():
    v = random.choice([True,False])
    if not v:
        raise  AirflowSkipException("Not meant to run")

test_op = PythonOperator(
    task_id='test_op', provide_context=True,
    python_callable=test, dag=dag)

action_op = DummyOperator(
    dag=dag,task_id='op_end',
    trigger_rule='all_success')

test_op >> action_op

