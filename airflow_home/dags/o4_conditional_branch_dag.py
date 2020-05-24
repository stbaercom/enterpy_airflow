from datetime import datetime
import random

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator

dag = DAG('o4_conditional_branch_dag',
          description='Conditional Branches',
          start_date=datetime(2020, 1, 1),
          schedule_interval=None)

op_start = DummyOperator(task_id='op_start', dag=dag)
op_alt1 = DummyOperator(task_id='op_alt1', dag=dag)
op_alt2 = DummyOperator(task_id='op_alt2', dag=dag)
op_alt3 = DummyOperator(task_id='op_alt3', dag=dag)

def make_choice():
    options = [f"op_alt{i}" for i in range(1,4)]
    return random.choice(options)

op_cond_branch = BranchPythonOperator(
    dag=dag,task_id='op_cond_branch',
    python_callable=make_choice)

op_end = DummyOperator(
    dag=dag,task_id='op_end',
    trigger_rule='none_failed_or_skipped')

op_start >> op_cond_branch >> [op_alt1,op_alt2,op_alt3] >> op_end

