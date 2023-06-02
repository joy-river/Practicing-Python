import pprint

import requests
from flight_data import FlightData
from datetime import datetime, timedelta

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.kiwi_city_url = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_flight_url = "https://api.tequila.kiwi.com/v2/search"
        self.tomorrow = datetime.now() + timedelta(days = 1)
        self.six_month = datetime.now() + timedelta(days= 180)
        self.flight_body = {
            "fly_from": "LON",
            "fly_to": "",
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.six_month.strftime("%d/%m/%Y"),
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "curr" : "GBP",
            "limit" : 1,
            "max_stopovers": 0
        }
        self.kiwi_key = {
            "apikey" : "WFuwp-_IqIVvOulwzyIt8Xwm2DJo4KkQ"
        }

    def search_city_code(self, city_data):
        city_codes = []
        for data in city_data:
            loc = requests.get(url=self.kiwi_city_url, params= {"term": data["city"]}, headers= self.kiwi_key).json()
            city_codes.append((loc["locations"][0]["code"]))
        return city_codes

    def search_flight(self, city_data):
        datas = []
        for data in city_data:
            self.flight_body["fly_to"] = data["iataCode"]
            f_data = requests.get(url=self.kiwi_flight_url, params=self.flight_body, headers=self.kiwi_key).json()
            try:
                datas.append(FlightData(f_data['data'][0]))
            except:
                self.flight_body["max_stopovers"] = 2
                f_data = requests.get(url=self.kiwi_flight_url, params=self.flight_body, headers=self.kiwi_key).json()
                self.flight_body["max_stopovers"] = 0
                try:
                    datas.append(FlightData(f_data['data'][0], stop_over=2))
                except:
                    datas.append(data["city"])
        return datas

