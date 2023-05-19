Key_OpenWeather = "badbd69dc67b8c7b154e5cd8a5ef0471"
YJ_lon = 128.62
YJ_lat = 36.80
# weather id < 700 : bring umb.

import requests

parameter = {
    "lat": YJ_lat,
    "lon": YJ_lon,
    "appid": Key_OpenWeather
}

weather = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
weather.raise_for_status()
data_list = weather.json()["list"]

rain = [item["weather"] for item in data_list[: 12]]

for weathers in rain:
    for ids in weathers:
        if ids["id"] > 800:
            print("Bring an umbrella.")