from flask import Flask
import psycopg2
from settings import db_name, password, user 
from events import Events
#enable cors for all use cases, probably temporary
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/mma')
def mma_data():
    conn = psycopg2.connect(dbname = db_name, user = user, password = password)
    cursor = conn.cursor()
    cursor.execute('select * from mma;')
    events_data= cursor.fetchall()

    parse_data = [Events(event = _event[1], headline= _event[2],venue = _event[3], date =_event[6] , latitude= _event[7], longitude = _event[8], color = _event[9], url =_event[10], org =_event[11]) for _event in events_data]
    events_dict = [event_.__dict__ for event_ in parse_data]

    return events_dict


app.run()   


