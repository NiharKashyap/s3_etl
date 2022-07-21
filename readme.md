
# S3, Lambda and RDS ETL Pipeline

Takes Json data from S3 bucket and saves to RDS Database

## Overview

Mock ETL Pipeline using Python Faker, AWS S3, AWS Lambda and 
AWS PostgreSQL RDS instance. Python script generates and Uploads
data to S3 bucket. AWS Lambda function is triggered whenever
a new file is uploaded to the S3 bucket. Lambda function reads
json data processes it using Pandas and inserts into RDS.


## Tasks

- [x]  Generate fake data with Faker
    - [x]  Convert Data to json format
- [x]  Upload Data to S3 bucket
- [x]  Read uploaded data from S3 using lambda
  - [x] Install required libraries in Lambda environment (Pandas, Psycopg2)
  - [x] Read environment variables in lambda
- [x]  Preprocessing in Pandas
- [x]  Save data to RDS


# Breakdown of each step

## Data generation and transmission

Use the Faker module to generate faker user data. The script `datagen.py` generates and sends fake data to S3 bucket. Amount of 
fake data to be generated is supplied as command line argument while running the script. The data is convertedd to json and sent
to S3

## S3 bucket trigger

Each time S3 bucket receives a new object lambda function is triggered. The data is converted to dataframe and
preprocessed using pandas

## Send data

The processed data is inserted into RDS. We are using PostgreSQL. So the psycopg2 connector is used to insert data to Aurora 
PostgreSQL instance