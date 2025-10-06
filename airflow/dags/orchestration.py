from attr.converters import default_if_none

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import sys
from docker.types import Mount
from airflow.providers.docker.operators.docker import DockerOperator

sys.path.append("/opt/airflow/api-request")

from insert_records import main

default_args = {

    'description': 'A DAG Orchestration of the data',
    'catchup': False,
    'start_date':datetime(2025,10,3)

}

dag = DAG(

    dag_id = 'weather-api-dbt-orchestration',
    default_args = default_args,
    schedule = timedelta(minutes = 1),

)

with dag:
    task1 = PythonOperator(

        task_id = 'Ingest_data_task',
        python_callable = main

    )
    task2 = DockerOperator(
        task_id = 'transform_data_task',
        image = 'ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command = 'run',
        working_dir = '/usr/app',
        mounts = [Mount(
            source='/home/ablaze/WSL-De/dbt/de_project',
            target = '/usr/app',
            type = 'bind'
        ),Mount(
            source = '/home/ablaze/WSL-De/dbt/profiles.yml',
            target = '/root/.dbt/profiles.yml',
            type = 'bind'
        ),],
        network_mode = 'wsl-de_my-network',
        docker_url ='unix://var/run/docker.sock',
        auto_remove = 'success'
    )

    task1 >> task2