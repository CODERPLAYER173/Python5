import datetime
import requests
import json
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_key = "JM013ZXFFVM7Z1F9"
Stock_price = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={api_key}&outputsize=compact').json()
open_price = float((Stock_price['Time Series (Daily)']['2026-04-15']["1. open"]))
close_price = float((Stock_price['Time Series (Daily)']['2026-04-15']["4. close"]))
if (close_price-open_price)/open_price*100 > 1:
    print(open_price)
    print(close_price)
    News = requests.get(
        f'https://gnews.io/api/v4/search?q={COMPANY_NAME}&lang=en&max=3&apikey=74c905cd51da75defb0a0d40428aa425')
    a = News.json()["articles"]
    for ar in range(0, 3):
        article = a[ar]
        print(f'NEWS {ar + 1}:' + article["title"])
        print(article["description"])
        print(article["content"])

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
import smtplib
email = "dekuuzumkai43@gmail.com"


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

