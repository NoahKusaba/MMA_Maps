import requests
from bs4 import BeautifulSoup
import datetime
from scrapers.models import handle_URL, valid_date
type = "boxing"

def scrape_wbc_events():
    soup = handle_URL("https://wbcboxing.com/en/eventos/list/", "WBC")
    fight_cards = soup.find_all(class_="type-tribe_events")
    list_events = []

    for fight_card in fight_cards:
        date = fight_card.find(class_="tribe-event-date-start").string
        date_object = datetime.datetime.strptime( date+" "+str(datetime.datetime.now().year), "%B %d %Y")
        if valid_date(date_object):
            headline = fight_card.find(class_="tribe-event-url").string.strip()
            event_name = fight_card.find(class_="tribe-events-list-event-description").find("p").string.strip()
            location = str(fight_card.find(class_="tribe-events-venue-details").find("a").string).split(", ")
            if len(location) ==1:
                country = location[0]
                city =""
            else:
                city = location[0]
                country = location[1]
            venue =""
            url = fight_card.find(class_="tribe-event-url")["href"]
            org = "WBC"
            list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object,"URL":url,"Org":org, "Type":type})

        else:
            pass

    return list_events

def scrape_wba_events():

    soup = handle_URL("https://www.wbaboxing.com/schedule-of-wba-title-fights","WBA")
    fight_cards = soup.find_all(class_="table-borderless")
    list_events = []
    
    for fight_card in fight_cards:
        date = fight_card.find(class_="custom-widget-header")

        breakpoint()
