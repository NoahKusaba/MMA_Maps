from colour import Color 
# Intention was for the markers on the map to be color coded depending on date. 
# Never Added to map
def marker_color(events):
    startColor= Color("green")
    colors = list(startColor.range_to(Color("red"),len(events)))

    for idx,event in enumerate(events):
        event.update({"Color":colors[idx]})
    return events