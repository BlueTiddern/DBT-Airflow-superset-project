import os

from api_requests import mock_fetch_data,fetch_data
import psycopg2
from dotenv import load_dotenv

def connect_to_db():
    print("Connecting to the postgreSQL database...")

    # loading the environment variables for the database connections
    load_dotenv()

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASS")

    try:
        # conn = psycopg2.connect( This code was not able to let airflow talk with postgres as the 5000 was not mapping to 5432
        #     host="localhost",
        #     port="5000",
        #     dbname=db_name,
        #     user=db_user,
        #     password=db_password
        # )
        conn = psycopg2.connect(host ='db',port='5432',dbname='db', user='db_user', password='pass')
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed{e}")
        raise
def create_table(conn):
    print("Creating table if not exist")

    try:
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE SCHEMA IF NOT EXISTS dev;
                       CREATE TABLE IF NOT EXISTS dev.raw_weather( 
                                id SERIAL PRIMARY KEY,
                                city TEXT,
                                temperature FLOAT,
                                weather_description TEXT,
                                wind_speed FLOAT,
                                time TIMESTAMP,
                                inserted_at TIMESTAMP DEFAULT NOW(),
                                utc_offset TEXT
                       );
                       """)
        conn.commit()
        print("Table created successfully")
    except psycopg2.Error as e:
        print(f"Table creation failed{e}")
        raise

def insert_records(conn,data):
    print("Inserting records weather data into the database..")
    try:
        weather = data["current"]
        location = data["location"]
        cursor = conn.cursor()
        cursor.execute("""
                INSERT INTO dev.raw_weather (city,
                                             temperature,
                                             weather_description,
                                             wind_speed,
                                             time,
                                             inserted_at,
                                             utc_offset) VALUES (%s, %s, %s, %s,%s, NOW(), %s)     
        """,(
             location['name'],
             weather['temperature'],
             weather['weather_descriptions'][0],
             weather['wind_speed'],
             location['localtime'],
             location['utc_offset']
        ))
        conn.commit()
        print("Records inserted successfully")
    except psycopg2.Error as e:
        print(f"Records insertion failed to insert into data base: {e}")
        raise

def main():
    try:
        #data = mock_fetch_data()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred during the execution: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")

main()

