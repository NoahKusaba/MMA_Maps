import psycopg2
from settings import db_name, password, user 

def commit_database(events, sport = 'MMA'):
    conn = psycopg2.connect(dbname = db_name, user = user, password = password, host='localhost', port= '5432')
    cursor = conn.cursor()

    cursor.execute(f"drop table if exists {sport}")
    conn.commit()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {sport}(
    id SERIAL PRIMARY KEY,
    Event VARCHAR(100),
    Headline VARCHAR(100), 
    Venue VARCHAR(100),
    City CHAR(100),
    Country CHAR(100),
    Date VARCHAR(100),
    Latitude FLOAT(25),
    Longitude FLOAT(25),
    Color VARCHAR(20),
    URL TEXT,
    Org VARCHAR(100)
    )""" )

    conn.commit()

    for event in events:
        try:
            cursor.execute(f"""insert into {sport} (Event, Headline, Venue, City, Country, Date, Latitude, Longitude, Color, URL, Org) Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,(event["Event"],event["Headline"],event["Venue"],event["City"],event["Country"],event["Date"],event["Coordinates"][0],event["Coordinates"][1],str(event["Color"])[6:-1],event["URL"],event["Org"]))
            conn.commit()
            
        except KeyError:
            breakpoint()
            pass



            
    conn.close()




    

