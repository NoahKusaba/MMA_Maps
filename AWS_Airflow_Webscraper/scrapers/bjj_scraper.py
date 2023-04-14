import datetime
from scrapers.models import handle_URL, valid_date
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

type = "bjj"

def scrape_ibjjf_events():
    url = "https://ibjjf.com/events/calendar"
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get(url)
    click_submit = driver.find_element(By.CLASS_NAME,"search-results-action")
    fight_cards = driver.find_elements(By.XPATH,"//div[@class='col-12 event-row']")
    list_events = []
    year = str(datetime.datetime.now().year)
    
    for fight_card in fight_cards:
        data = fight_card.text.split('\n')
        if len(data[0].split('-')) == 2:
            date = (data[0].split('-')[0] +" "+ year).strip().replace("*","")
            date_object = datetime.datetime.strptime(date,'%b %d %Y')
            end_date = (data[0].split('-')[-1] +" "+ year).strip().replace("*","")
            end_date_object = datetime.datetime.strptime(end_date,'%b %d %Y')

        else: 
            date = (data[0] +" "+ year).strip().replace("*","")
            date_object = datetime.datetime.strptime(date,'%b %d %Y')
            end_date_object = 0
        if valid_date(date_object,end_date_object):
            headline = data[1][0:-5]
            event_name = headline
            venue = data[2].split(', ')[0]
            city = data[2].split(', ')[-1]
            country = ""
            org = 'ibjjf'
            list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object,"URL":url,"Org":org, "Type":type})
        else:
            pass
    driver.quit()
    return list_events

def scrape_adcc_events():
    soup = handle_URL("https://adcombat.com/adcc-events/","ADCC")
    fight_cards = soup.find_all(class_="col-xs-12 row-eq-height")
    list_events= []
    org = "adcc"
    for fight_card in fight_cards:
        date_data = fight_card.find(class_="rw-event-date").get_text().replace("\n\n","").split("\n")
        date = date_data[0] +' '+ date_data[1]+' '+ date_data[-1]
        date_object = datetime.datetime.strptime(date,"%b %d %Y")
        if valid_date(date_object):
            event_name = fight_card.find(class_="entry-title").find("a").string.replace("2023","")
            headline = event_name
            location = fight_card.find(class_="rw-event-location").string.split(", ")
            country = location[-1].split(",\n")[-1]
            city = location[-1].split(",\n")[0]
            venue = location[0]
            url = fight_card.find(class_="entry-title").a["href"]
            list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object,"URL":url,"Org":org, "Type":type})
        else:
            pass
    return list_events
