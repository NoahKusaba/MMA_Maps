from commit_database import commit_database
from scrapers.models import *
from transformations import marker_color
sample_commit = [{'Event': 'UFC 284', "Headline":"testtest", 'Venue': 'RAC Arena','City': 'Perth', 'Country': 'Australia', 'Date': '02/12/2023', 
'Coordinates':[-31.948421,115.85194], "Color":1212321, "URL":"adslkfjasdlfkj.com", "Org":"UFC","Type":"MMA"},{'Event': 'UFC 284', "Headline":"testtest", 'Venue': 'RAC Arena','City': 'Perth', 'Country': 'Australia', 'Date': '02/12/2023', 
'Coordinates':[-31.948421,115.85194], "Color":1212321, "URL":"adslkfjasdlfkj.com", "Org":"UFC","Type":"MMA"},{'Event': 'UFC 284', "Headline":"testtest", 'Venue': 'RAC Arena','City': 'Perth', 'Country': 'Australia', 'Date': '02/12/2023', 
'Coordinates':[-31.948421,115.85194], "Color":1212321, "URL":"adslkfjasdlfkj.com", "Org":"UFC","Type":"MMA"},{'Event': 'UFC 284', "Headline":"testtest", 'Venue': 'RAC Arena','City': 'Perth', 'Country': 'Australia', 'Date': '02/12/2023', 
'Coordinates':[-31.948421,115.85194], "Color":1212321, "URL":"adslkfjasdlfkj.com", "Org":"UFC","Type":"MMA"},{'Event': 'UFC 284', "Headline":"testtest", 'Venue': 'RAC Arena','City': 'Perth', 'Country': 'Australia', 'Date': '02/12/2023', 
'Coordinates':[-31.948421,115.85194], "Color":1212321, "URL":"adslkfjasdlfkj.com", "Org":"UFC","Type":"MMA"},{'Event': 'UFC 284', "Headline":"testtest", 'Venue': 'RAC Arena','City': 'Perth', 'Country': 'Australia', 'Date': '02/12/2023', 
'Coordinates':[-31.948421,115.85194], "Color":1212321, "URL":"adslkfjasdlfkj.com", "Org":"UFC","Type":"MMA"}]

def test_commit():
    commit_database(sample_commit,table = "test_events")

def test_color():
    returnColor = marker_color(sample_commit)
    color = str(returnColor[-1]["Color"])
    assert color ==  "red"


