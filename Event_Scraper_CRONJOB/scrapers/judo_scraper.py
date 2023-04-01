import datetime
from scrapers.models import handle_URL, valid_date
type = "judo"
org = "judo" # not realistic to get unique pictures for event
def scrape_usajudo_events():
    main_url = "https://www.teamusa.org/usa-judo/events?SearchText=&SelectedEventTypes=9211ab49-9fea-4c86-8650-ce8d64eaec48&SelectedEventTypes=0a5da8a2-92c6-4274-83ab-d390f08c9a44&startDate=&endDate=&zipcode=&Radius=25&RegionId=&StateId=&CountryId="
    soup = handle_URL(main_url,"USA Judo")
    page_count = soup.find(class_="paging").find_all("li")
    list_events = []
    
    for page in range(1, len(page_count) -2):
        soup = handle_URL(main_url+str(page),"USA Judo")
        fight_cards = soup.find_all(class_="striped-grid-row")

        for fight_card in fight_cards[1::]:
            date_total = fight_card.find(class_="event-date-cell").p.string.split(", ")

            if " - " in date_total[0]:
                # case more than 1 day event 
                date = date_total[0].split(" - ")[0] + " " + date_total[-1]
                date_object = datetime.datetime.strptime(date,"%B %d %Y")

                # case (March 31 - April 02) vs (March 27 - 28) 
                if len(date_total[0].split(" - ")[1].split(" ")) == 2:
                    end_date = date_total[0].split(" - ")[1]+" "+ date_total[-1]
                    end_date_object = datetime.datetime.strptime(end_date,"%B %d %Y")
                else:
                    end_date = date_total[0].split(" - ")[0].split(" ")[0] +" "+ date_total[0].split(" - ")[1] + " " +date_total[-1]
                    end_date_object = datetime.datetime.strptime(end_date,"%B %d %Y")
            else:
                # Case 1 day event. 
                date = date_total[0] +" "+date_total[-1]
                date_object = datetime.datetime.strptime(date,"%B %d %Y")
                end_date = 0
                end_date_object

            if valid_date(date_object, end_date_object):
                headline = fight_card.find(class_="event-title-cell").a.string
                event_name = headline
                venue=""
                url = fight_card.find(class_="event-title-cell").a["href"]
                location = fight_card.find(class_="event-location-cell").p.string.split(", ")
                city = location[0]
                country = location[-1]
                list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object,"URL":url,"Org":org, "Type":type}) 
            else:
                pass

    breakpoint()
    return list_events