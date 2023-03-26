import requests
from settings import CordKey

#TOMTOM Geocode APi
def returnCoordinate(name):

    for event in name:

        if event["City"] == "Bangkok":
            event.update({"Coordinates":[13.8757,100.66738]})  # exception handeling for Lumpinee Boxing Stadium
            
        else:
            url ="https://api.tomtom.com/search/2/geocode/"
            #url = "https://api.radar.io/v1/search/autocomplete?query=" failed radar api
            url+= event["Venue"] +", "+event["City"]+ ", " + event["Country"] +".json" +f"?key={CordKey}"

            response = requests.get(url)
        
            if response.status_code !=200:
                print("Error GeoCode")
                print(response)
                exit()        

            data= response.json()
            
            cords = list(data["results"][0]["position"].values())
            event.update({"Coordinates":cords})

        
    return name