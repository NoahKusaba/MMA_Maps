import os
from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv('TESTDB')
user = os.getenv('TESTUSER')
password = os.getenv('TESTPASSWORD')
hostname = os.getenv('TESTHOST')