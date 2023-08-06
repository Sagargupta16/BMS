import yaml
import pymongo

with open("config/secrets.yml", "r") as stream:
    secrets = yaml.safe_load(stream)

mongodb_host = secrets["mongodb"]["host"]
mongodb_port = secrets["mongodb"]["port"]
mongodb_database = secrets["mongodb"]["database"]
mongodb_connection_string = secrets["mongodb"]["connection_string"]

client = pymongo.MongoClient(mongodb_connection_string)

db = client[mongodb_database]

def get_db():
    return db

def get_student_collection():
    return db["students"]

