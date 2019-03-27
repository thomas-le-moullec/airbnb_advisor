import numpy as np
import psycopg2 as pg
from psycopg2 import sql
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

def listing_number_by_host(cur, nbr, listing_table_name):
    statement = "select count(distinct host_id) from {} WHERE host_listings_count=" + str(nbr)
    cur.execute(
        sql.SQL(statement)
        .format(sql.Identifier(listing_table_name)))
    return (cur.fetchone()[0])

def table_exists(table_name, cur):
    statement = "SELECT EXISTS ( SELECT 1 FROM information_schema.tables WHERE table_name='" +  table_name + "')"
    cur.execute(
        sql.SQL(statement)
	.format(sql.Identifier(table_name)))
    return cur.fetchone()[0]

def process_data(table_name, connection):
    print("Connecting to Database")
    cur = connection.cursor()
    create_table_query = 'CREATE TABLE IF NOT EXISTS processed_data ' + '''(
            city CHAR(2) NOT NULL,
            PRIMARY KEY (city),
	    listing_number INT,
	    average_price REAL,
	    available_listing_average REAL,
	    entire_home_number INT,
            private_room_number INT,
            shared_room_number INT,
            host_number INT,
            estimated_income REAL,
            single_listing_number INT,
            bed_number_average REAL,
            review_per_month_average REAL,
            host_with_one_listing_number INT,
            host_with_two_listing_number INT,
            host_with_three_listing_number INT,
            host_with_four_listing_number INT,
            host_with_five_listing_number INT
    )'''
    listing_table_name = 'listings_' + table_name
    calendar_table_name = 'calendar_' + table_name
    if (table_exists(listing_table_name, cur) == 0 or table_exists(calendar_table_name, cur) == 0):
	print('Table does not exist')
	connection.close()
        print('Connection closed.')
        return
    cur.execute(create_table_query)
    cur.close()
    connection.commit()
    cur = connection.cursor()
    cur.execute(
        sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(listing_table_name)))
    lst_nbr = cur.fetchone()[0]
    cur.execute(
	sql.SQL("SELECT COUNT(distinct host_id) FROM {}").format(sql.Identifier(listing_table_name)))
    host_nbr = cur.fetchone()[0]
    cur.execute(
        sql.SQL("SELECT AVG(price) from {}").format(sql.Identifier(calendar_table_name)))
    avg_price = cur.fetchone()[0]
    cur.execute(
        sql.SQL("SELECT AVG(beds) FROM {}").format(sql.Identifier(listing_table_name)))
    bed_nbr_avg = cur.fetchone()[0]
    cur.execute(
        sql.SQL("select count(*) from {} WHERE room_type like 'P%%'").format(sql.Identifier(listing_table_name)))
    private_room_number = cur.fetchone()[0]
    cur.execute(
        sql.SQL("select count(*) from {} WHERE room_type like 'E%%'").format(sql.Identifier(listing_table_name)))
    entire_room_number = cur.fetchone()[0]
    cur.execute(
        sql.SQL("select count(*) from {} WHERE room_type like 'S%%'").format(sql.Identifier(listing_table_name)))
    shared_nbr = cur.fetchone()[0]
    cur.execute(
        sql.SQL("select count(*) from {} WHERE host_listings_count=1").format(sql.Identifier(listing_table_name)))
    unique_listings = cur.fetchone()[0]
    hw1 = listing_number_by_host(cur, 1, listing_table_name)
    hw2 = listing_number_by_host(cur, 2, listing_table_name)
    hw3 = listing_number_by_host(cur, 3, listing_table_name)
    hw4 = listing_number_by_host(cur, 4, listing_table_name)
    hw5 = listing_number_by_host(cur, 5, listing_table_name)
    cur.execute(
       	sql.SQL("select avg(reviews_per_month) from {}").format(sql.Identifier(listing_table_name)))
    avg_rv_p_m = cur.fetchone()[0]
    cur.execute(
        sql.SQL("select count(*) from {}").format(sql.Identifier(calendar_table_name)))
    total = cur.fetchone()[0]
    cur.execute(
        sql.SQL("select count(*) from {} where available=false").format(sql.Identifier(calendar_table_name)))
    res = cur.fetchone()[0]
    avl_lst_avg = (float(res) / float(total)) * 100
    estimated_income = (avg_price * (100 - avl_lst_avg) / 100.0) * 30.5

    cur.execute('''insert into processed_data values (%s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING''',
    (table_name[0:2], lst_nbr, avg_price, avl_lst_avg, entire_room_number, private_room_number,
    shared_nbr, host_nbr, estimated_income, unique_listings, bed_nbr_avg, avg_rv_p_m,
    hw1, hw2, hw3, hw4, hw5,))
    cur.execute("commit;")
    print("Loaded data into {}".format(table_name))
    connection.close()
    print("DB connection closed.")


def __main__():
    try:
        connection = connect_to_database()
        table_name = sys.argv[1]
        process_data(table_name, connection)
    except (Exception, pg.DatabaseError) as error:
        print ("Error: ", error)

__main__()
