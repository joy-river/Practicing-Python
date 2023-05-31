# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
# from notification_manager import NotificationManager
import os
import requests
import pprint
from datetime import datetime
from Ui import User

dm = DataManager()
fs = FlightSearch()
# nm = NotificationManager()



# a = [item for item in dm.city_data if item["iataCode"] == ""]
# if len(a) > 0:
#     dm.put_codes(fs.search_city_code(a))
#     dm.get_city_data()
#
# flight_datas = fs.search_flight(dm.city_data)
#
# for data in flight_datas:
#     try:
#       print(f"{data.cityTo}-{data.cityCodeTo} : ${data.price}")
#     except:
#       print("There is No direct Flight from London to {data}")


user = User()
dm.post_user_info(user)