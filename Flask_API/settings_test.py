import os
from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv('TESTDB')
user = os.getenv('TESTUSER')
password = os.getenv('TESTPASSWORD')
host = os.getenv('TESTHOST')