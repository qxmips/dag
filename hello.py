from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import airflow
def hello_world():
    print('Hello World')

hello_dag = DAG('hello',
    description='demo',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval='@daily')

task = PythonOperator(
    task_id='hello_world',
    python_callable=hello_world,
    dag=hello_dag)
