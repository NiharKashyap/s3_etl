from http import client
import boto3
import os
from dotenv import load_dotenv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="File name to upload")

load_dotenv()


AWS_ACCESS_KEY_ID= os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')


def upload_file(file_name):
    
    try:

        client = boto3.client('s3',
                    aws_access_key_id = AWS_ACCESS_KEY_ID,
                    aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        with open(file_name, "rb") as f:
            client.upload_fileobj(f, BUCKET_NAME, file_name)
            print('Uploaded file: ' + file_name)
    except Exception as e:
        print('Exception in Uploading: ',e)
        

if __name__=='__main__':
    
    args = parser.parse_args()
    print(args.file_name)

    upload_file("data/"+args.file_name)
    

    