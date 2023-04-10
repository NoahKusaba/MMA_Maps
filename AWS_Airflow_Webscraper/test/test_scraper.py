from scrapers import scrape_bellator_events, scrape_ufc_events, scrape_one_events, scrape_wbc_events, scrape_wba_events, scrape_ibf_events, scrape_wbo_events


def check_event(events,org):
    breakpoint()
    for event in events:
        count = 0
        if event["City"]:
            count+=1 
        if event["Country"]:
            count+=1 
        assert count >=1, f"failed data {org}"


def test_valid_scraper():

    events = scrape_ufc_events()
    
    check_event(events,"UFC")

    events = scrape_bellator_events()
    check_event(events, "Bellator")

    events = scrape_one_events()
    check_event(events, "ONE")

    events = scrape_wbc_events()
    check_event(events,"WBC")
    
    events = scrape_wba_events()
    check_event(events,"WBA")

    events = scrape_ibf_events()
    check_event(events,"IBF")

    events = scrape_wbo_events()
    check_event(events,"WBO")

