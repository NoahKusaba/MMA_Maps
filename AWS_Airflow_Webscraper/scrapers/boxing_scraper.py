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
            list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object.strftime('%Y-%m-%d'),"URL":url,"Org":org, "Type":type})

        else:
            pass

    return list_events

def scrape_wba_events():
    soup = handle_URL("https://www.wbaboxing.com/schedule-of-wba-title-fights","WBA")
    fight_cards = soup.find_all(class_="table-borderless")
    list_events = []
    url = "https://www.wbaboxing.com/schedule-of-wba-title-fights"
    for fight_card in fight_cards:
        date = fight_card.find(class_="custom-widget-header").find("h4").find_all("br")[-1].string.split("-")[0].strip()
        date_object = datetime.datetime.strptime(date, "%B %d, %Y")
        if valid_date(date_object):
            event_name = " ".join(fight_card.find(class_="custom-widget-header").get_text(separator="<br>").split("<br>")[0:-1]).strip().replace("  "," ").replace("  "," ")
            fighters = fight_card.find_all("h3")
            fighter_1 = fighters[0].string.strip().split(" ")[0] +" "+ fighters[0].string.strip().split(" ")[-1]
            fighter_2 = fighters[-1].string.strip().split(" ")[0] +" "+ fighters[-1].string.strip().split(" ")[-1]
            headline = fighter_1 + " vs " + fighter_2
            venue=""
            location = fight_card.find(class_="custom-widget-header").get_text(separator="<br>").split("<br>")[-1].split(' - ')[-1].strip()
            if len(location) ==2:
                city = location.split(", ")[0]
                country =location.split(", ")[-1]
            else:
                city = ""
                country =location
            org = "WBA"
            
            list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object.strftime('%Y-%m-%d'),"URL":url,"Org":org, "Type":type})
        else:
            pass
    return list_events
            
def scrape_ibf_events():
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get("https://www.ibf-usba-boxing.com/index.php/schedule?view=matchs")
    click_submit  = driver.find_element(By.CLASS_NAME,"btn").click()
    fight_cards = driver.find_elements(By.XPATH,'//article/div[@class="row"]')
    url = "https://www.ibf-usba-boxing.com/index.php/schedule?view=matchs"
    list_events = []
    for fight_card in fight_cards:
        date = fight_card.find_element(By.XPATH,'./strong').text[4::]
        date_object = datetime.datetime.strptime(date,"%B %d, %Y")
        if valid_date(date_object):
            event_name = fight_card.find_element(By.XPATH,".//h4[@class='text-white text-uppercase']").text

            fighter_1= fight_card.find_elements(By.XPATH,".//h3/a")[0].text.replace("\n"," ")
            fighter_2 = fight_card.find_elements(By.XPATH,".//h3/a")[-1].text.replace("\n"," ")
            headline = fighter_1 +" vs "+fighter_2

            location = fight_card.find_element(By.XPATH,".//div/p").text.split(", ")
            if len(location) == 3:
                city = location[1][5::]

                country = location[2].split("\n")[0]
                # venue= location[2].split("\n")[1] Gives promotion name and corrupts coordinate
                venue = ""
            else:
                location = fight_card.find_element(By.XPATH,".//div/p").text.split("\n")
                
                country = location[1]
                city = ""
                venue = ""
                # venue = location[-1]
            org = "IBF"

            list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object.strftime('%Y-%m-%d'),"URL":url,"Org":org, "Type":type}) 
        else:
            pass
    driver.quit()
    return list_events


def scrape_wbo_events():
    soup = handle_URL("https://wboboxing.com/","WBO")
    fight_cards = soup.find_all(class_="col main-fight")
    list_events = []
    url = "https://wboboxing.com/"
    org ="WBO"
    for fight_card in fight_cards:
        date = fight_card.find(class_="m-0").string.strip()
        date_object = datetime.datetime.strptime(date,"%B %d, %Y")
        if valid_date(date_object):
            event_name = fight_card.find(class_="card-title").get_text().replace("\t","").replace("  "," ")
            fight =  fight_card.find_all(class_= "fighter-info")
            fighter_1 = fight[0].get_text().replace("\n","").replace("  "," ")
            fighter_2 = fight[1].get_text().replace("\n","").replace("  "," ")
            headline = fighter_1 + " vs " + fighter_2
            venue = ""
            location = fight_card.find(class_="card-footer").find(class_="text-muted").string.split(", ")
            city = location[0]
            country = location[-1]
            if city =="Venue TBD" and country == "Venue TBD":
                pass
            else:
                list_events.append({"Event":event_name, "Headline":headline, "Venue":venue, "City":city,"Country":country,"Date":date_object.strftime('%Y-%m-%d'),"URL":url,"Org":org, "Type":type}) 
        else:
            pass
    return list_events