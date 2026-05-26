import pandas as pd
import json
import requests
a = pd.read_csv("country_mun_data.csv")
def country_research(country=input("Enter the country Name ").capitalize()):
    country_research_fields = [
        "capital",
        "population",
        "borders",
        "area",
        "timezones"
    ]
    response = requests.get(f'https://restcountries.com/v3.1/name/{country}')
    data = response.json()
    for x in country_research_fields:
        print(f'{x}": "{data[0][x]}')
    b =a.loc[a["Country"] == country]
    print("Rivals:"+b["Rivals"].iloc[0])
    print("Allies: "+b["Allies"].iloc[0])
    print("Organization Afialiated: "+b["Organizations"].iloc[0])
country_research()