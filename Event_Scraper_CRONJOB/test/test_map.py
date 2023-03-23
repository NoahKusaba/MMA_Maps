from coordinate3 import returnCoordinate




def test_returnCoordinate():
    correct_outputJson = {'Event': 'UFC 284', 'Sport': 'MMA', 'City': 'Perth', 'Country': 'Australia', 'Venue': 'RAC Arena', 'Date': '02/12/2023', 
'coordinates': [-31.948421, 115.85194]}
    input_venue = {"Event":"UFC 284",
    "Sport":"MMA",
    "City":"Perth",
    "Country":"Australia",
    "Venue":"RAC Arena",
    "Date":"02/12/2023"
    }
    output_json = returnCoordinate(input_venue)
    assert output_json == correct_outputJson, "Radar API returns wrong output"


