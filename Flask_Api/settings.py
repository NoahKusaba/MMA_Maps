import os
from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv('DATABASE_NAME')
user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')