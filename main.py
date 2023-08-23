import requests
from twilio.rest import Client
import datetime as dt


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = 'AC46efb628867a73cc1a31614e4075c74d'
auth_token = '4ff3b15af50281002e92ecfc754db7db'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "NGMYA8NO19VXXIJV"
NEWS_API_KEY = "cdcc8d94c06f4e56a8c3a51de11afb90"

DATE = dt.datetime.today

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()

yesterday_closing_price = data["Time Series (Daily)"]["2023-08-10"]["4. close"]
day_before_yesterday_closing_price = data["Time Series (Daily)"]["2023-08-09"]["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

diff_percentage = round((difference/float(yesterday_closing_price)) * 100)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if diff_percentage > 0:

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

    formated_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)

    for article in formated_articles:
        message = client.messages.create(
            from_='+12292807900',
            body=article,
            to='+918875187588'
        )
    print("message sent")
    
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

