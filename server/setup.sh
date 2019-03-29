#!/bin/bash
yum update -y
sudo pip install psycopg2
sudo pip install panda
sudo pip install numpy
aws s3 cp s3://tslemoullec-airbnb-listings/Berlin/calendar_be_ma_2019.csv.gz  .
aws s3 cp s3://tslemoullec-airbnb-listings/Berlin/listings_be_ma_2019.csv.gz  .
gunzip listings_be_ma_2019.csv.gz
gunzip calendar_be_ma_2019.csv.gz
sudo yum install postgresql
sudo yum install sqlalchemy
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
export NVM_DIR="$HOME/.nvm"
bash
nvm install node
