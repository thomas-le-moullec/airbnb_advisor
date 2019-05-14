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
    create_table_query = 'CREATE TABLE IF NOT EXISTS ' + tableName + ''' (
    id INT,
PRIMARY KEY (id),
host_is_superhost REAL,
host_total_listings_count REAL,
host_has_profile_pic REAL,
host_identity_verified REAL,
latitude REAL,
longitude REAL,
property_type TEXT,
room_type TEXT,
bathrooms REAL,
bedrooms REAL,
beds REAL,
bed_type TEXT,
price REAL,
guests_included REAL,
minimum_nights REAL,
maximum_nights REAL,
review_scores_rating REAL,
review_scores_accuracy REAL,
review_scores_cleanliness REAL,
review_scores_checkin REAL,
review_scores_communication REAL,
review_scores_location REAL,
review_scores_value REAL,
renting_ratio REAL
)'''
    cur.execute(create_table_query)
    cur.close()
    connection.commit()
    cur = connection.cursor()
    f = open(filename, "r")
    cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(tableName), f)
    cur.execute("commit;")
    print("Loaded data into {}".format(tableName))
    connection.close()
    print("DB connection closed.")

def create(l, superCsv):
    listingsList = pd.read_csv(l)
    # keeping is simpler than dropping since we have a lot of useless features
    listingsList = listingsList[['id',
                             'host_is_superhost','host_total_listings_count','host_has_profile_pic',
                             'host_identity_verified','latitude','longitude',
                             'property_type','room_type','bathrooms','bedrooms','beds','bed_type',
                             'price','guests_included','minimum_nights',
                             'maximum_nights','review_scores_rating','review_scores_accuracy',
                             'review_scores_cleanliness','review_scores_checkin',
                             'review_scores_communication','review_scores_location','review_scores_value']]
    # handling boolean values
    listingsList['host_is_superhost'] = listingsList['host_is_superhost'].replace({"t": 1.0, "f": 0.0})
    listingsList['host_has_profile_pic'] = listingsList['host_has_profile_pic'].replace({"t": 1.0, "f": 0.0})
    listingsList['host_identity_verified'] = listingsList['host_identity_verified'].replace({"t": 1.0, "f": 0.0})

    # simplifying some values
    listingsList['room_type'] = listingsList['room_type'].replace({"Entire home/apt": "Entire", "Private room": "Room", "Shared room": "Shared"})
    listingsList['bed_type'] = listingsList['bed_type'].replace({"Real Bed": "Bed", "Pull-out Sofa": "Sofa"})
    # converting price to number
    listingsList['price'] = listingsList['price'].str[1:]
    listingsList['price'] = listingsList['price'].str.replace(',', '')
    listingsList['price'] = listingsList['price'].astype(float)
    listingsList = listingsList.fillna(listingsList.mean())
    ratio = superCsv.groupby("listing_id")['available'].mean()
    ratio = 1 - pd.DataFrame(ratio)
    ratio.columns=['renting_ratio']
    ratio.index.names = ['id']
    ratio.reset_index(level=0, inplace=True)
    listingsList = pd.merge(listingsList, ratio, how='inner')
    return listingsList

def __main__():
    try:
        connection = connectToDatabase()
        listingsFilename = sys.argv[1]
        city = listingsFilename[9:-12]
        superCsv = pd.read_csv("calendar_" + city + ".csv")
        listingsList = create(listingsFilename, superCsv)
        listingsList.to_csv("listings_" + city + ".csv", index=False)
        uploadInTable("listings_" + city, "listings_" + city + ".csv", connection)
    except (Exception, pg.DatabaseError) as error:
        print ("Error: ", error)

__main__()
