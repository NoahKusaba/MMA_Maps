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
    if event_name == 'USA Judo':
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
        }
    else:
        headers = {'User-Agent':"Custom"}
    
    response = requests.get(url,headers = headers)
    print('Headers ', headers)
    if response.status_code !=200:
        print(response)
        print(response.content)
        print(response.status_code)
        print(f"Error Fetching {event_name}")
        exit()
    else:
        return(BeautifulSoup(response.content,"html.parser"))