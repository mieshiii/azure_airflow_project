from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import date
from reddit_script import azure_airflow_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': date.today(),
    'email': ['mieseliel.delacruz@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

#prepare the DAG via default args
dag = DAG(
  'azure_airflow_etl',
  default_args=default_args,
  description='Azure Airflow ETL pipeline'
)

#callback twitter_etl function via PythonOperator
run_etl = PythonOperator(
  task_id='azure_airflow_etl',
  python_callable=azure_airflow_etl,
  dag=dag,
)