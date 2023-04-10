import requests
from settings import CordKey

#TOMTOM Geocode APi
def returnCoordinate(name):

    for event in name:
        if event["City"] == "Bangkok":
            event.update({"Coordinates":[13.8757,100.66738]})  # exception handeling for Lumpinee Boxing Stadium
        elif event["City"] == "Barueri":
            event.update({"Coordinates":[-23.5070384,-46.8679179]}) 



        else: 
            if event["City"] == "Wein":
                event["City"] = "Vienna"
            url ="https://api.tomtom.com/search/2/geocode/"

            #url = "https://api.radar.io/v1/search/autocomplete?query=" failed radar api
            if event["Type"] == "bjj":
                url += event["City"]+ ", " + event["Country"] +".json" +f"?key={CordKey}"
            else:
                url+= event["Venue"] +", "+event["City"]+ ", " + event["Country"] +".json" +f"?key={CordKey}"

            response = requests.get(url)
        
            if response.status_code !=200:
                print("Error GeoCode")
                print(response)
                exit()        

            data= response.json()
            try:
                cords = list(data["results"][0]["position"].values())
                event.update({"Coordinates":cords})
            except IndexError:
                breakpoint()        
    return name