STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import os
import requests
from twilio.rest import Client

alpha_api_key = "KVD1FFS0GLJRO3MK"
news_api_key = "b5b36c3ee885424e8446b91956e15f41"
params = {
    "stock_param": {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": alpha_api_key
    },
    "news_param": {
        "q": COMPANY_NAME,
        "language": "en",
        "page" : 3,
        "apikey": news_api_key
    }
}

## STEP 1: Use https://www.alphavantage.co
stock_price = requests.get(url="https://www.alphavantage.co/query", params=params["stock_param"])
stock_price.raise_for_status()
stock = stock_price.json()["Time Series (Daily)"]
prices = []

for value in stock.values():
    if len(prices) < 2:
        prices.append(float(value["5. adjusted close"]))

if abs(prices[0] - prices[1]) > prices[1] / 20:
    print("Get News")
else:
    print(prices)
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news = requests.get(url="https://newsapi.org/v2/everything", params=params["news_param"])
news.raise_for_status()
print(news.json())



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
