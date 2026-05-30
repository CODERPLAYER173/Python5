from flask import Flask, render_template,request
import pandas as pd
import requests
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Country_info/',methods=['GET','POST'])

def country_info():
    result = None

    if request.method == "POST":
        country = request.form["Country"]


        a = pd.read_csv("country_mun_data.csv")

        response = requests.get(
            f'https://restcountries.com/v3.1/name/{country}'
        )

        data = response.json()[0]

        b = a.loc[a["Country"] == country]

        result = {
            "country": country,
            "capital": data.get("capital", ["N/A"])[0],
            "population": data.get("population", "N/A"),
            "borders": data.get("borders", []),
            "area": data.get("area", "N/A"),
            "timezones": data.get("timezones", []),
            "rivals": b["Major_Rivals"].iloc[0],
            "allies": b["Allies"].iloc[0],
            "organizations": b["Organizations"].iloc[0]
        }

    return render_template("Country.html", result=result)