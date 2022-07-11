import boto3
from dotenv import load_dotenv
import os
from connect import engine
import psycopg2

load_dotenv()


cur = engine.cursor()

cur.execute("select * from employee")
record = cur.fetchall()
print(record)
