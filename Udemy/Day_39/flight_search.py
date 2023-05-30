import requests
from datetime import datetime, timedelta

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.kiwi_city_url = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_flight_url = "https://api.tequila.kiwi.com/v2/search"
        self.tomorrow = datetime.now() + timedelta(days = 1)
        self.flight_body = {
            "fly_from": "LON",
            "fly_to": "",
            "date_from": self.now.strftime("%d/%m/%Y"),
            "date_to": self.now.strftime("%M")
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

