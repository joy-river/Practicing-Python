import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.city_data = None
        self.sheety_url = "https://api.sheety.co/b522a052a88212ddc882983bd34104a6/flightDeals/prices"
        self.get_city_data()
    def put_codes(self, city_codes):
        for i in range(len(city_codes)):
            requests.put(url=f"{self.sheety_url}/{i + 2}", json={"price": {"iataCode":city_codes[i]}})

    def get_city_data(self):
        self.city_data = requests.get(url=self.sheety_url).json()["prices"]
