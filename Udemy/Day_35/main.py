Key_OpenWeather = "badbd69dc67b8c7b154e5cd8a5ef0471"
YJ_lon = 128.62
YJ_lat = 36.80
# weather id < 700 : bring umb.

import os
import requests
from twilio.rest import Client

parameter = {
    "lat": YJ_lat,
    "lon": YJ_lon,
    "appid": Key_OpenWeather
}

weather = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
weather.raise_for_status()
data_list = weather.json()["list"]

rain = [item["weather"][0] for item in data_list[: 12]]
rain_today = False
for i in rain:
    if i["id"] < 700:
        rain_today = True

account_sid = os.environ.get("twilio_account_sid")
auth_token = os.environ.get("twilio_auth_token")
client = Client(account_sid, auth_token)

if rain_today:
    message = client.messages \
        .create(
        body="Today is rainy day. Bring an umbrella!",
        from_='+12543584761',
        to='+821098299803'
    )
    print(message.status)
