
import requests

question_data = []
request = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data = request.json()
for x in range(0,10):
    question_data.append(data["results"][x])
