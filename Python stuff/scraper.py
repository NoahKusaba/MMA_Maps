import requests
from bs4 import BeautifulSoup
import datetime

def scrape_bellator_events():
    response = requests.get("https://www.bellator.com/event")

    if response.status_code !=200:
        print("Error Fetching Bellator")
        exit()

    else:
        soup = BeautifulSoup(response.content, "html.parser")
        fight_cards = soup.find_all(class_="UpcomingEventCardstyles__UpcomingEventCardContainer-gmhvif-0 dnctcc")
        list_events = []
        #{"Event":, "Venue":, "City":,"Country":,"Date":,"URL":,"Headline"}
        for fight_card in fight_cards:

            date = fight_card.find("span").string.split(" ")
            date.pop(0)
            date_object = datetime.datetime.strptime(" ".join(date)+ " 2023", "%B %d %Y")

            url = "https://www.bellator.com" +str(fight_card.find("a"))[9:19]     # URL for each event. 
            elements = fight_card.find_all("p")
            event_Name = elements[0].string
            headline = elements[1].string
            venue = elements[2].string
            city = elements[3].string.split(", ")[0]
            country = elements[3].string.split(", ")[1]

            list_events.append({"Event":event_Name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object,"URL":url,"Org":"Bellator"})
       
        return list_events


def scrape_ufc_events():
    response = requests.get("https://www.ufc.com/events#events-list-upcoming")
    if response.status_code !=200:
        print("Error UFC")
        exit()
    else:
        soup = BeautifulSoup(response.content, "html.parser")
        fight_cards = soup.find_all(class_="l-listing__item")
        list_events = []
        #{"Event":, "Venue":, "City":,"Country":,"Date":,"URL":,"Headline"}

        for fight_card in fight_cards:
            elements_date = fight_card.find(class_="c-card-event--result__date tz-change-data")

            date = elements_date.find("a").string[5:-15]
            date_object = datetime.datetime.strptime(date.rstrip()+" 2023","%b %d / %I:%M %p %Y")
            currentDate = datetime.datetime.now()

            if currentDate > date_object:
                pass
            else:
                headline = fight_card.find(class_="c-card-event--result__headline").find("a").string
                event_Name = "UFC "+ headline
                venue = fight_card.find("h5").string.strip()
                try:
                    city = fight_card.find(class_="locality").string
                except AttributeError:
                    pass

                country = fight_card.find(class_="country").string
                url = "https://www.ufc.com" + str(fight_card.find(class_="c-card-event--result__headline").find("a")["href"])

                list_events.append({"Event":event_Name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object,"URL":url,"Org":"UFC"})

        return list_events

def scrape_one_events():
    response = requests.get("https://www.onefc.com/events/#upcoming")

    if response.status_code !=200:
        print("Error ONE")
        exit()

    else:

        soup = BeautifulSoup(response.content, "html.parser")
        fight_cards = soup.find(id="upcoming-events-section").find_all(class_="simple-post-card")

        list_events = []
        #{"Event":, "Venue":, "City":,"Country":,"Date":,"URL":,"Headline"}
        for fight_card in fight_cards:
  
            url = str(fight_card.find(class_="image")["href"])
            event_response = requests.get(url)
            event_soup = BeautifulSoup(event_response.content, "html.parser")
            elements = event_soup.find(class_="info-content")

            date = (elements.find(class_="day").string + elements.find_all(class_="time")[1].string).split(" ")
            date = date[0] + " " + date[1] +" 2023"
            date_object = datetime.datetime.strptime(date,"%b %d %Y")
            event_Name = elements.find(class_="title use-letter-spacing-hint").string[1:]
            country = ""
            headline =""
            try:
                headline = event_soup.find(class_="versus").string[1:-1]
            except AttributeError:
                pass
            
            try:
                venue = elements.find(class_="event-location").string.split(", ")[0]
            except AttributeError:
                pass
            try:
                city = elements.find(class_="event-location").string.split(", ")[1]
            except AttributeError:
                pass
            list_events.append({"Event":event_Name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object,"URL":url,"Org":"ONE"})

        return list_events
    