import requests
from bs4 import BeautifulSoup
import datetime

currentDate = datetime.datetime.now()

def valid_date(date_obj, end_date_obj = 0):
    if end_date_obj and end_date_obj > currentDate: return True 
    elif not end_date_obj and date_obj > currentDate: return True 
    else: return False

def handle_URL(url,event_name):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0' } if event_name == 'USA Judo' else {'User-Agent':"Custom"}; print('Headers ', headers)
    response = requests.get(url,headers = headers)
    if response.status_code !=200:
        print(f"Error Fetching {event_name} with response {response}, response content {response.content}, response status_code {response.status_code}")
        exit()
    else: return(BeautifulSoup(response.content,"html.parser"))