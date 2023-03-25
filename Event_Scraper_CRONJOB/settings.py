import os
from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv('DATABASE_NAME')
user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
hostname = os.getenv('HOST')
CordKey = os.getenv('TOMTOMKEY')