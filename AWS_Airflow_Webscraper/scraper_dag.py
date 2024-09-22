from transformations import marker_color, returnCoordinate
from commit_database import * 
from scrapers import *
from datetime import datetime
from airflow.decorators import dag, task
import pendulum
#This is pretty self explanitory 

@dag(
    schedule = '@weekly',
    start_date = pendulum.datetime(2023,4,20,tz="UTC"),
    catchup = False,
    tags = ['event_maps'],
)
def scrape_and_upload():

    @task()
    def upload_mma():
        scrape_mma = scrape_one_events() +scrape_bellator_events() +scrape_ufc_events()
        return scrape_mma

    @task()
    def upload_bjj():
        scrape_bjj = scrape_ibjjf_events() + scrape_adcc_events()
        return scrape_bjj

    @task()
    def upload_judo():
        scrape_judo = scrape_ijf_events()
        return scrape_judo

    @task()
    def upload_boxing():
        scrape_boxing =scrape_wbc_events() +scrape_wba_events() + scrape_wbo_events() # + scrape_ibf_events() 
        return scrape_boxing

    @task()
    def get_cords(mma, bjj, judo, boxing):
        total_events = mma + bjj + judo +boxing
        return returnCoordinate(total_events)
    
    @task()
    def upload_events(total_events):
        total_events_sorted = sorted(total_events, key = lambda event:datetime.strptime(event["Date"],'%Y-%m-%d'))
        total_events_color = marker_color(total_events_sorted)
        commit_database(total_events_color)
        
    mma = upload_mma()
    bjj = upload_bjj()
    judo = upload_judo()
    boxing = upload_boxing()
    total_events = get_cords(mma = mma, bjj= bjj, judo = judo, boxing = boxing)
    upload_events(total_events)

scrape_fighting_events = scrape_and_upload()




#muay thai, Broken
# location_tf = scrape_tf_events()
# location_mmt = scrape_mmt_events()
# location_lf = scrape_lf_events()

# tf_location_cord = returnCoordinate(location_tf)
# mmt_location_cord = returnCoordinate(location_mmt)
# lf_location_cord = returnCoordinate(location_lf)

######################################################################
# Folium map for those interested 
# import folium 
# import webbrowser

# f = folium.Figure(width=1000,height = 500)
# map = folium.Map(tiles = 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',attr='My Data Attribution', max_bounds=True, zoom_start = 1, min_zoom = 2).add_to(f)
# for x in total_events_color:
#     folium.Marker(x["Coordinates"],icon = folium.Icon(icon_color=x['Color'].hex_l), popup=x["Event"]).add_to(map)
# output_file = "map.html"
# map.save(output_file)
# webbrowser.open(output_file)