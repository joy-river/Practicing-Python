# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
import os
import requests
from datetime import datetime

dm = DataManager()
fs = FlightSearch()
fd = FlightData()
nm = NotificationManager()

a = [item for item in dm.city_data if item["iataCode"] == ""]
dm.put_codes(fs.search_city_code(a))

dm.get_city_data()
fs.search_flight(dm.city_data)
