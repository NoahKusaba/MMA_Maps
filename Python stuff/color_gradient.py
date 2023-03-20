from colour import Color 
import datetime

def marker_color(events):
    list_dates = sorted(list(set([x["Date"] for x in events]))) # small to large
    orange= Color("green")
    colors = list(orange.range_to(Color("red"),len(list_dates)))
    date_colors = {list_dates[x]:colors[x] for x in range(len(list_dates))}
    for event in events:
        event.update({"Color":date_colors[event["Date"]]})
    
    return events