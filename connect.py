import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


database = os.environ.get("database")
user = os.environ.get("user")
password = os.environ.get("password")
host=os.environ.get("host")
port=os.environ.get("port")


engine = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)