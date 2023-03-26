import requests
from coordinate import *
from color_gradient import *
import folium 
import webbrowser
from Event_Scraper_CRONJOB.mma_scraper import scrape_bellator_events, scrape_ufc_events, scrape_one_events

location_bellator = scrape_bellator_events()
location_ufc = scrape_ufc_events()
location_one = scrape_one_events()

one_location_cord = returnCoordinate(location_one)
ufc_location_cord = returnCoordinate(location_ufc)
bellator_location_cord = returnCoordinate(location_bellator)

print(location_one + location_bellator)

map = folium.Map(zoom_start=1,tiles = 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',attr='My Data Attribution')


for x in bellator_location_cord:
    folium.Marker(x["coordinates"],icon = folium.Icon(icon_color='#FFFF00'), popup=x["Event"]).add_to(map)

# for x in ufc_location_cord:
#     folium.Marker(x["coordinates"],icon = folium.Icon(color="red"),popup=x["Event"]).add_to(map)

# for x in one_location_cord:
#     folium.Marker(x["coordinates"],icon = folium.Icon(color="gold"),popup=x["Event"]).add_to(map)

output_file = "map2.html"
map.save(output_file)
webbrowser.open(output_file)
