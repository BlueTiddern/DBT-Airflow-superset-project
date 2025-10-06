-- Create the airflow user given in the slq alchemy conn
CREATE USER airflow WITH PASSWORD 'airflow';

-- create the airflow db and assign the airflow as owner
CREATE DATABASE airflow_db OWNER airflow;