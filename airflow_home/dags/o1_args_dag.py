from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def patch_path():
    import os
    import sys
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    sys.path.insert(0, path)


patch_path()
import b_dag_support as ds

dag = DAG('o1_arglog_dag',
          description='Python Operator with Argument',
          start_date=datetime(2018, 1, 1),
          schedule_interval=None,
          catchup=False
          )

def arglog(*args, **kwargs):
    ds.dump_pp(kwargs, "kwargs.txt")
    ds.dump_pp(args, "args.txt")

arglog_op = PythonOperator(
    task_id='arglog_task',
    provide_context=True,
    python_callable=arglog,
    op_args=["a1", "a2"],
    op_kwargs={"k1": "v1", "k2": "v2"},
    dag=dag)

arglog_op
