from settings import CordKey
import googlemaps
#GoogleMaps Geocode APi

gmaps = googlemaps.Client(key = CordKey)

def returnCoordinate(name):

    for event in name:
        geocode_query = event['City'] + ' '+ event['Country'] + ' '+ event['Venue']
        geocode_result = gmaps.geocode(geocode_query)
        cords = list(geocode_result[0]['geometry']['location'].values())
        event.update({"Coordinates":cords})

    return name