from faker import Faker
import json
from datetime import datetime
from s3_upload import upload_file
import argparse
faker = Faker()

def generate_data():
    name = faker.name()
    age = faker.random_int(min=18, max=80)
    address = faker.address()
    zip = faker.zipcode()
    gender = faker


parser = argparse.ArgumentParser()
parser.add_argument("count", help="Count of data to generate")


for i in range(1):
    profile = faker.profile()
    with open("data/" + profile['username'] + '.json', 'a') as prof:
        del profile['current_location']
        profile['birthdate']=datetime.strftime(profile['birthdate'], '%Y-%m-%d')
        json.dump(profile, prof, indent=4)
        prof.close()
        upload_file("data/" + profile['username'] + '.json')