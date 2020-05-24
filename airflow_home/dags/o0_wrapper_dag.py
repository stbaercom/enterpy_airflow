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

dag = DAG('o0_wrapper_dag',
          description='Python Task Wrapper DAG',
          start_date=datetime(2018, 1, 1),
          schedule_interval=None,
          catchup=False)

get_prices_operator = PythonOperator(
    dag=dag,task_id='get_prices_task',
    python_callable=ds.get.main)

calc_stats_operator = PythonOperator(
    dag=dag, task_id='calc_stats_task',
    python_callable=ds.calc.main)

do_report_operator = PythonOperator(
    dag=dag,task_id='do_report_task',
    python_callable=ds.rep.main,)

get_prices_operator >> calc_stats_operator >> do_report_operator



