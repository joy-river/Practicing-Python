# # API == 음식점 메뉴판
#
# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()[""]
# print(data)

import requests

my_lat = 51
my_lng = 0

param = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params= param)
response.raise_for_status()
print(response.json()["results"]["sunrise"].split("T")[1].split("+")[0])