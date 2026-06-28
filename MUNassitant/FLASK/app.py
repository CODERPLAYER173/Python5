from flask import Flask, render_template,request
import pandas as pd
import requests as r
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
        response = r.get(
            f'https://api.restcountries.com/countries/v5?q={country}',
            headers={'Authorization': 'Bearer rc_live_bb50cbc1bbe0408c9432b533661b19db'}
        )
        data = response.json()

        b = a.loc[a["Country"] == country.upper()]
        result = {
            "country": country,
            "capital": data.get("capital", ["N/A"]),
            "population": data.get("population", "N/A"),
            "borders": data.get("borders", []),
            "area": data.get("area", "N/A"),
            "timezones": data.get("timezones", []),
            "rivals": b["Major_Rivals"].iloc[0],
            "allies": b["Allies"].iloc[0],
            "organizations": b["Organizations"].iloc[0],
        }

    return render_template("Country.html", result=result)


@app.route('/Speech_generator/' ,methods = ['GET','POST'])
def speech_generator():
    if request.method == "POST":
        country = request.form["country"]
        committee = request.form["Committee"]
        agenda = request.form["agenda"]
        time = request.form["time"]
        topic = request.form["topic"]

        from google import genai

        client = genai.Client(api_key="AIzaSyAHHD7CCw6qdejyvomiDpflpVxZ5L29KNY")

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"Make a Mun speech of topic:{topic},committee:{committee},agenda:{agenda},time:{time},country:{country}"
        )
    else:
        response = None
    return render_template("speech.html", response=response)
@app.route('/resolution_drafter/' ,methods = ['GET','POST'])
def resolution_generator():
    if request.method == "POST":
        country = request.form["country"]
        committee = request.form["Committee"]
        agenda = request.form["agenda"]
        time = request.form["time"]
        topic = request.form["topic"]
        speech = request.form["speech"]

        from google import genai

        client = genai.Client(api_key="AIzaSyAHHD7CCw6qdejyvomiDpflpVxZ5L29KNY")

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"Make a Mun resolution of topic:{topic},committee:{committee},agenda:{agenda},time:{time},country:{country} and refer to the speech{speech}"
        )
    else:
        response = None
    return render_template("resolution drafter.html", response=response)
@app.route('/poi_generator/' ,methods = ['GET','POST'])
def poi_generator():
    if request.method == "POST":
        country = request.form["country"]
        committee = request.form["Committee"]
        agenda = request.form["agenda"]
        time = request.form["time"]
        topic = request.form["topic"]
        speech = request.form["speech"]

        from google import genai

        client = genai.Client(api_key="AIzaSyAHHD7CCw6qdejyvomiDpflpVxZ5L29KNY")

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"Make a Mun resolution of topic:{topic},committee:{committee},agenda:{agenda},time:{time},country:{country} and refer to the speech{speech}"
        )
    else:
        response = None
    return render_template("resolution drafter.html", response=response)