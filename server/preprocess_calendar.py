import numpy as np
import datetime
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

def monthDelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)

def removeLongTermCalendar(csvToAdd):
    addUpTo = max(csvToAdd['date'])
    addUpToDate = datetime.datetime.strptime(addUpTo, '%Y-%m-%d')
    addUpToDate = monthDelta(addUpToDate, -10)
    addUpTo = addUpToDate.strftime("%Y-%m-%d")
    csvToAdd = csvToAdd[csvToAdd['date'] < addUpTo]
    return csvToAdd

def addToSuperCsv(superCsv, csvToAdd):
    keepUpTo = min(csvToAdd['date'])
    superCsv = superCsv[superCsv['date'] < keepUpTo]
    # Remove the next 10 months in the future.
    csvToAdd = removeLongTermCalendar(csvToAdd)
    superCsv = pd.concat([superCsv, csvToAdd])
    return superCsv

def connectToDatabase():
    dbName = os.getenv("DBNAME")
    dbPwd = os.getenv("DBPWD")
    dbUser = os.getenv("DBUSER")
    dbPort = os.getenv("DBPORT")
    dbHost = os.getenv("DBHOST")
    return pg.connect("dbname="+dbName+" user="+dbUser+" password="+dbPwd+" host=" + dbHost + " port="+dbPort)

def uploadInTable(tableName, filename, connection):
    print("Connecting to Database")
    cur = connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS ' + tableName + ''' (
            listing_id INT NOT NULL,
            date DATE NOT NULL,
            PRIMARY KEY (listing_id , date),
            available BOOL,
            price REAL
            )'''
    cur.execute(query)
    cur.close()
    connection.commit()
    cur = connection.cursor()
    f = open(filename, "r")
    cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(tableName), f)
    cur.execute("commit;")
    print("Loaded data into {}".format(tableName))
    connection.close()
    print("DB connection closed.")

def preprocessCsv(superCsvname):
    superCsv = pd.read_csv(superCsvname)
    superCsv['available'] = superCsv['available'].replace({"t": True, "f": False})
    superCsv['price'] = superCsv['price'].str[1:]
    superCsv['price'] = superCsv['price'].str.replace(',', '')
    superCsv['price'] = superCsv['price'].astype(float)
    return superCsv


def __main__():
    try:
        connection = connectToDatabase()
        calendarFilename = sys.argv[1]
        city = calendarFilename[9:-12]
        superCsv = pd.read_csv("calendar_" + city + ".csv")
        csvToAdd = preprocessCsv(calendarFilename)
        superCsv = addToSuperCsv(superCsv, csvToAdd)
        superCsv.to_csv("calendar_" + city + ".csv", index=False)
        uploadInTable("calendar_" + city, "calendar_" + city + ".csv", connection)
    except (Exception, pg.DatabaseError) as error:
        print ("Error: ", error)

__main__()

