import psycopg2
from settings import db_name, password, user, hostname

def commit_database(events,table = "events"):
    """
    events: 
        - List of dictionaries containing event information to upload to DB
    table: 
        - String designating event-type to determine which table to upload to. 
    """
    conn = psycopg2.connect(dbname = db_name, user = user, password = password, host=hostname, port= '5432')
    cursor = conn.cursor()
    cursor.execute(f"drop table if exists {table};")
    conn.commit()
    cursor.execute(f"drop index if exists event_type")
    conn.commit()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table}(
    id SERIAL PRIMARY KEY,
    Event VARCHAR(100),
    Headline VARCHAR(100), 
    Venue VARCHAR(100),
    City CHAR(50),
    Country CHAR(50),
    Date VARCHAR(100),
    Latitude FLOAT(25),
    Longitude FLOAT(25),
    Color VARCHAR(20),  
    URL TEXT,
    Org VARCHAR(20),
    TYPE VARCHAR(20)
    )""" )
    conn.commit()

    # only need to stringify color object.
    for event in events:
        try:
            cursor.execute(f"""insert into {table} (Event, Headline, Venue, City, Country, Date, Latitude, Longitude, Color, URL, Org, Type) Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
            """,(event["Event"],event["Headline"],event["Venue"],event["City"],event["Country"],event["Date"],event["Coordinates"][0],event["Coordinates"][1],str(event["Color"]),event["URL"],event["Org"],event["Type"]))
            conn.commit()
        except KeyError:
            breakpoint()
            pass

    cursor.execute(f"create index event_type ON {table} (Type)")
    conn.commit()   
    conn.close()




    

