from transformations import marker_color, returnCoordinate
from commit_database import * 
from scrapers import *

#mma
# location_one = scrape_one_events()
# location_bellator = scrape_bellator_events()
# location_ufc = scrape_ufc_events()


# one_location_cord = returnCoordinate(location_one)
# bellator_location_cord = returnCoordinate(location_bellator)
# ufc_location_cord = returnCoordinate(location_ufc)


#boxing
# location_wbc = scrape_wbc_events()
# location_wba = scrape_wba_events()
# location_ibf = scrape_ibf_events()
# location_wbo = scrape_wbo_events()

# wbc_location_cord = returnCoordinate(location_wbc)
# wba_location_cord = returnCoordinate(location_wba)
# ibf_location_cord = returnCoordinate(location_ibf)
# wbo_location_cord = returnCoordinate(location_wbo)

#bjj
# location_ibjjf = scrape_ibjjf_events()
# location_adcc = scrape_adcc_events()

#judo
location_usajudo_events =scrape_usajudo_events()

#muay thai
# location_tf = scrape_tf_events()
# location_mmt = scrape_mmt_events()
# location_lf = scrape_lf_events()

# tf_location_cord = returnCoordinate(location_tf)
# mmt_location_cord = returnCoordinate(location_mmt)
# lf_location_cord = returnCoordinate(location_lf)

total_ufc = one_location_cord  + bellator_location_cord + ufc_location_cord 
total_boxing = wbc_location_cord +wba_location_cord +ibf_location_cord + wbo_location_cord
total_events = total_ufc + total_boxing
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