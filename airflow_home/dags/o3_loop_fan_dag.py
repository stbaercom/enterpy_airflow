from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('loop_fan_dag',
          description='Loops and Fanout',
          start_date=datetime(2020, 1, 1),
          schedule_interval=None,
          )

op_start = DummyOperator(task_id='op_start', dag=dag)
op_b1 = DummyOperator(task_id='op_b1', dag=dag)
op_b2 = DummyOperator(task_id='op_b2', dag=dag)

op_join1 = DummyOperator(task_id='op_join1', dag=dag)

op_start >> [op_b1, op_b2] >> op_join1

op_end = DummyOperator(task_id='op_end', dag=dag)

for i in range(5):
    op = DummyOperator(task_id=f'op_loop_{i}', dag=dag)
    op_join1 >> op >> op_end
