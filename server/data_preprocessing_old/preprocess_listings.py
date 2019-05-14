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

def toBool(item):
    if (item == 'f'):
        return 0
    elif (item == 't'):
	return 1
    return item

def create_proper_csv(filename):
    processed_filename = filename[:-4] + '_processed.csv'
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        lines = list(reader)
        for row in lines:
	    row[28] = toBool(row[28])
	    row[35] = toBool(row[35])
	    row[36] = toBool(row[36])
	    row[50] = toBool(row[50])
	    row[76] = toBool(row[76])
	    row[93] = toBool(row[93])
	    row[96] = toBool(row[96])
	    row[97] = toBool(row[97])
	    row[99] = toBool(row[99])
	    row[100] = toBool(row[100])
            row[48] = row[48].replace('$', '')
            row[49] = row[49].replace('$', '')
            row[54] = row[54].replace('$', '')
            row[55] = row[55].replace('$', '')
            row[60] = row[60].replace('$', '')
            row[61] = row[61].replace('$', '')
            row[62] = row[62].replace('$', '')
            row[63] = row[63].replace('$', '')
            row[64] = row[64].replace('$', '')
            row[66] = row[66].replace('$', '')
            row[73] = row[73].replace('$', '')
            row[74] = row[74].replace('$', '')
            row[105] = row[105].replace('$', '')
	    row[48] = row[48].replace(',', '')
            row[49] = row[49].replace(',', '')
            row[54] = row[54].replace(',', '')
            row[55] = row[55].replace(',', '')
            row[60] = row[60].replace(',', '')
            row[61] = row[61].replace(',', '')
            row[62] = row[62].replace(',', '')
            row[63] = row[63].replace(',', '')
            row[64] = row[64].replace(',', '')
            row[66] = row[66].replace(',', '')
            row[73] = row[73].replace(',', '')
            row[74] = row[74].replace(',', '')
            row[105] = row[105].replace(',', '')

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
    id INT,
PRIMARY KEY (id),
listing_url TEXT,
scrape_id REAL,
last_scraped DATE,
name TEXT,
summary TEXT,
space TEXT,
description TEXT,
experiences_offered TEXT,
neighborhood_overview TEXT,
notes TEXT,
transit TEXT,
access TEXT,
interaction TEXT,
house_rules TEXT,
thumbnail_url TEXT,
medium_url TEXT,
picture_url TEXT,
xl_picture_url TEXT,
host_id INT,
host_url TEXT,
host_name TEXT,
host_since DATE,
host_location TEXT,
host_about TEXT,
host_response_time TEXT,
host_response_rate TEXT,
host_acceptance_rate TEXT,
host_is_superhost BOOL,
host_thumbnail_url TEXT,
host_picture_url TEXT,
host_neighbourhood TEXT,
host_listings_count INT,
host_total_listings_count INT,
host_verifications TEXT,
host_has_profile_pic BOOL,
host_identity_verified BOOL,
street TEXT,
neighbourhood TEXT,
neighbourhood_cleansed TEXT,
neighbourhood_group_cleansed TEXT,
city TEXT,
state TEXT,
zipcode TEXT,
market TEXT,
smart_location TEXT,
country_code TEXT,
country TEXT,
latitude REAL,
longitude REAL,
is_location_exact BOOL,
property_type TEXT,
room_type TEXT,
accommodates INT,
bathrooms REAL,
bedrooms REAL,
beds INT,
bed_type TEXT,
amenities TEXT,
square_feet TEXT,
price REAL,
weekly_price REAL,
monthly_price REAL,
security_deposit REAL,
cleaning_fee REAL,
guests_included INT,
extra_people REAL,
minimum_nights INT,
maximum_nights INT,
minimum_minimum_nights INT,
maximum_minimum_nights INT,
minimum_maximum_nights INT,
maximum_maximum_nights INT,
minimum_nights_avg_ntm REAL,
maximum_nights_avg_ntm REAL,
calendar_updated TEXT,
has_availability BOOL,
availability_30 INT,
availability_60 INT,
availability_90 INT,
availability_365 INT,
calendar_last_scraped DATE,
number_of_reviews INT,
number_of_reviews_ltm INT,
first_review DATE,
last_review DATE,
review_scores_rating INT,
review_scores_accuracy INT,
review_scores_cleanliness INT,
review_scores_checkin INT,
review_scores_communication INT,
review_scores_location INT,
review_scores_value INT,
requires_license BOOL,
license TEXT,
jurisdiction_names TEXT,
instant_bookable BOOL,
is_business_travel_ready BOOL,
cancellation_policy TEXT,
require_guest_profile_picture BOOL,
require_guest_phone_verification BOOL,
calculated_host_listings_count TEXT,
calculated_host_listings_count_entire_homes INT,
calculated_host_listings_count_private_rooms INT,
calculated_host_listings_count_shared_rooms INT,
reviews_per_month REAL
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
        listings_filename = sys.argv[1]
        processed_csv = create_proper_csv(listings_filename)
        table_name = listings_filename[:-7]
        upload_data_in_table(table_name, processed_csv, connection)
    except (Exception, pg.DatabaseError) as error:
        print ("Error: ", error)

__main__()
