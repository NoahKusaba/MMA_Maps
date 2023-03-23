from flask import Flask
import psycopg2
from settings import db_name, password, user,host
from events import Events
#enable cors for all use cases, probably temporary
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route('/mma')

def mma_data():
    accepted_events = ["mma", "boxing"]

    conn = psycopg2.connect(dbname = db_name, user = user, password = password, host = host)
    cursor = conn.cursor()

    

    cursor.execute('select * from mma')

    events_data= cursor.fetchall()
    parse_data = [Events(event = _event[1], headline= _event[2],venue = _event[3], date =_event[6] , latitude= _event[7], longitude = _event[8], color = _event[9], url =_event[10], org =_event[11]) for _event in events_data]
    events_dict = [event_.__dict__ for event_ in parse_data]
    return events_dict


app.run(host = "0.0.0.0")   


    # if type.find("-") != -1:
    #     for index in type.split('-'):
    #         if index not in accepted_events:
    #             return 

    # list_queries = type.split("-")


    # conn = psycopg2.connect(dbname = db_name, user = user, password = password, host = host)
    # cursor = conn.cursor()

    