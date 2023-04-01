import requests
from bs4 import BeautifulSoup
import datetime

currentDate = datetime.datetime.now()

def valid_date(date_obj, end_date_obj = 0):
    if end_date_obj:
        if end_date_obj > currentDate:
            return True
        else:
            return False
    else:
        if date_obj > currentDate:
            return True
        else:
            return False

def handle_URL(url,event_name):
    headers = {'User-Agent':"Custom"}
    response = requests.get(url,headers = headers)
    if response.status_code !=200:
        print(f"Error Fetching {event_name}")
        exit()
    else:
        return(BeautifulSoup(response.content,"html.parser"))