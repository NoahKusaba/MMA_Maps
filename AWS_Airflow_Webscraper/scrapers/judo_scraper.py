from datetime import datetime
from scrapers.models import handle_URL, valid_date
type = org = "judo"
year = datetime.now().year
def scrape_ijf_events():
    main_url = "https://www.ijf.org/calendar?year=2023&month=&age=world_tour&type=comp"
    soup = handle_URL(main_url,"USA Judo")
    fight_cards = soup.find_all('tr')
    list_events = []
    for fight_card in fight_cards:
        #pass if hidden row
        if not fight_card.attrs['class']:
            month = fight_card.find(class_='calendar-date--short__month').string
            days = fight_card.find(class_='calendar-date--short__days').string
            
            if '-' in days:
                date_object = datetime.strptime(month+ " "+days.split(' - ')[0] +" "+str(year),'%B %d %Y')
                end_date_object = datetime.strptime(month+ " "+days.split(' - ')[1] +" "+str(year),'%B %d %Y')
            else:
                date_object = datetime.strptime(month+ " "+days +" "+str(year),'%B %d %Y')
                end_date_object = 0

            if valid_date(date_object, end_date_object):
                headline = fight_card.find(class_="event-link-title").string.strip()
                event_name = headline
                venue=""
                url = fight_card.find(class_="event-link")["href"]
                location = fight_card.find(class_='calendar-location').find(class_='event-link').get_text().strip().split(', ')
                city = location[1]
                country = location[0]
                list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object.strftime('%Y-%m-%d'),"URL":url,"Org":org, "Type":type}) 
