import boto3
from dotenv import load_dotenv
import os


load_dotenv()

AWS_ACCESS_KEY_ID= os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')

                    
client = boto3.client('rds-data', aws_access_key_id = AWS_ACCESS_KEY_ID,
                    aws_secret_access_key = AWS_SECRET_ACCESS_KEY)