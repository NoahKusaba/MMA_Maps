from colour import Color 

def marker_color(events):
    startColor= Color("green")
    colors = list(startColor.range_to(Color("red"),len(events)))

    for idx,event in enumerate(events):
        event.update({"Color":colors[idx]})
    return events