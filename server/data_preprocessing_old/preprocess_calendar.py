import numpy as np
import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd
import csv
import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def connect_to_database():
    dbName = os.getenv("DBNAME")
    dbPwd = os.getenv("DBPWD")
    dbUser = os.getenv("DBUSER")
    dbPort = os.getenv("DBPORT")
    dbHost = os.getenv("DBHOST")
    return pg.connect("dbname="+dbName+" user="+dbUser+" password="+dbPwd+" host=" + dbHost + " port="+dbPort)

def create_proper_csv(filename):
    processed_filename = filename[:-4] + '_processed.csv'
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        lines = list(reader)
        for row in lines:
	    if (row[2] == "f"):
                row[2] = 0
            elif (row[2] == "t"):
                row[2] = 1
            row[3] = row[3].replace('$', '')
            row[4] = row[4].replace('$', '')
            row[3] = row[3].replace(',', '')
            row[4] = row[4].replace(',', '')

    with open(processed_filename, 'w+') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    writeFile.close()
    csvFile.close()
    return processed_filename


def upload_data_in_table(table_name, filename, connection):
    print("Connecting to Database")
    cur = connection.cursor()
    create_table_query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ''' (
            listing_id INT NOT NULL,
            date DATE NOT NULL,
            PRIMARY KEY (listing_id , date),
            available BOOL,
            price REAL,
            adjusted_price REAL,
            minimum_date INT,
            maximum_date INT
            )'''
    cur.execute(create_table_query)
    cur.close()
    connection.commit()
    cur = connection.cursor()
    f = open(filename, "r")
    cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
    cur.execute("commit;")
    print("Loaded data into {}".format(table_name))
    connection.close()
    print("DB connection closed.")


def __main__():
    try:
        connection = connect_to_database()
        calendar_filename = sys.argv[1]
        processed_csv = create_proper_csv(calendar_filename)
        table_name = calendar_filename[:-7]
        upload_data_in_table(table_name, processed_csv, connection)
    except (Exception, pg.DatabaseError) as error:
        print ("Error: ", error)

__main__()

