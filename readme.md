
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
- [ ]  Preprocessing in Pandas
- [ ]  Save data to RDS