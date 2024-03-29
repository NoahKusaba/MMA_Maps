from flask import Flask
import psycopg2
from settings import db_name, password, user,host
from api.models import Events
#enable cors for all use cases, probably temporary
from flask_cors import CORS
accepted_events = ["mma", "boxing","judo","bjj"]

'''
    - Rest API
        - Outputs event data by sport.
        - Can output multiple event types of seperated by "-"
            - Valid Examples (Order doesn't matter):
                - '/mma'
                - '/mma-boxing'
                - '/mma-boxing-judo'
'''
def create_api():
    app = Flask(__name__)
    CORS(app) 

    @app.route('/')
    def home():
        return f'Accepted Events:, {accepted_events}'

    @app.route('/<type>')
    def mma_data(type):
        
        insertType = ""
        
        if type.find("-") != -1:
            for index in type.split('-'):
                if index not in accepted_events:
                    pass
                else:
                    stringInsert = str(index)
                    insertType += ' Type = ' +f"'{stringInsert}'" +" or"
            insertType= insertType[0:-2]
        elif type in accepted_events:
            insertType = ' Type = ' + f"'{type}'"

        else:
            raise KeyError("Incorrect Query")
        
        conn = psycopg2.connect(dbname = db_name, user = user, password = password, host = host)
        cursor = conn.cursor()
        sql_query= f'select * from events where {insertType};'
        cursor.execute(sql_query)
        events_data= cursor.fetchall()
        parse_data = [Events(event = _event[1], headline= _event[2],venue = _event[3], date =_event[6] , latitude= _event[7], longitude = _event[8], color = _event[9], url =_event[10], org =_event[11]) for _event in events_data]
        events_dict = [event_.__dict__ for event_ in parse_data]
        return events_dict
    
    return app