import boto3
from dotenv import load_dotenv
import os
from connect import engine
import psycopg2

load_dotenv()

#TODO: 1. Take Data from faker and insert  

cur = engine.cursor()

cur.execute("select * from employee")
record = cur.fetchall()
print(record)
