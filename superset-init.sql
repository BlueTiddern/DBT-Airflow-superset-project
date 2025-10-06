-- Create the airflow user given in the slq alchemy conn
CREATE USER superset WITH PASSWORD 'superset';

-- create the airflow db and assign the airflow as owner
CREATE DATABASE superset_db OWNER superset;


-- Create the airflow user given in the slq alchemy conn
CREATE USER examples WITH PASSWORD 'examples';

-- create the airflow db and assign the airflow as owner
CREATE DATABASE examples_db OWNER examples;