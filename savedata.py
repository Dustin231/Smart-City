#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error

global id
global temperature
global sensor
global luminance
global datetime
global doorbell
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all_tasks(conn):
 
    cur = conn.cursor()
    cur.execute("SELECT * FROM readings;")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def insert_data(conn, temperature, luminance, sensor, doorbell, datetime):
   
    cur = conn.cursor()
    
    cur.execute("INSERT INTO readings (temperature,luminance, sensor, doorbell, datetime) values (?,?,?,?,?)", (temperature, luminance, sensor, doorbell, datetime))

    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
def main():
    database = "sensor_rd.db"
 
    # create a database connection
    conn = create_connection(database)
    doorbell = "0"
    temperature = "12.0"
    luminance = "12.0"
    datetime = "1201"
    sensor = "1"
	
    with conn:
        
        #print("1. Inserts sensor data")
        insert_data(conn, temperature, luminance, sensor, doorbell, datetime)
 
        print("2. Query all tasks")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()