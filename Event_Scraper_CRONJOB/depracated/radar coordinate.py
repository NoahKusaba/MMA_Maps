import requests


#Radar Geocode APi
def returnCoordinate(name):
    
    print(name)
    for event in name:
        url ="https://api.radar.io/v1/geocode/forward?query="
        #url = "https://api.radar.io/v1/search/autocomplete?query="
        url+= event["Venue"].replace(" ","") +"+"+event["City"].replace(" ","")+ "+" + event["Country"].replace(" ","") 
     
        print(url) 
        header = {
            "Authorization": "prj_live_pk_e8ef2a90e162349ee59e539535bd0848fb472230"
        }
        
        response = requests.get(url,headers =header)
   
        if response.status_code !=200:
            print("Error GeoCode")
            exit()        

        data= response.json()
        print(data)
        cord= data["addresses"][0]["geometry"]["coordinates"]
        event.update({"coordinates":[cord[1],cord[0]]})

    return name