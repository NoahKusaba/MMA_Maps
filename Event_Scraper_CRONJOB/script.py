from coordinate import *
from color_gradient import *
from commit_database import * 
from mma_scraper import scrape_bellator_events, scrape_ufc_events, scrape_one_events

location_bellator = scrape_bellator_events()
location_ufc = scrape_ufc_events()
location_one = scrape_one_events()


bellator_location_cord = returnCoordinate(location_bellator)
ufc_location_cord = returnCoordinate(location_ufc)
one_location_cord = returnCoordinate(location_one)


total_events = one_location_cord  + bellator_location_cord + ufc_location_cord 
total_events_sorted = sorted(total_events, key = lambda event:event["Date"])
total_events_color = marker_color(total_events_sorted)

commit_database(total_events_color)



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


