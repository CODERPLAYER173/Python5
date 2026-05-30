import pandas as pd
import json
import requests


def country_research(country):
    import pandas as pd
    import requests
    country_research_fields = [
        "capital",
        "population",
        "borders",
        "area",
        "timezones"
    ]
    a = pd.read_csv("country_mun_data.csv")
    response = requests.get(f'https://restcountries.com/v3.1/name/{country}')
    data = response.json()
    for x in country_research_fields:
        print(f'{x}": "{data[0][x]}')
    b =a.loc[a["Country"] == country]
    print("Rivals:"+b["Major_Rivals"].iloc[0])
    print("Allies: "+b["Allies"].iloc[0])
    print("Organization Afialiated: "+b["Organizations"].iloc[0])
