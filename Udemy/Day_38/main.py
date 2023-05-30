import os
import requests
from datetime import datetime

nut_api_id = os.environ.get("nut_api_id")
nut_api_key = os.environ.get("nut_api_key")
nut_api_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

nut_header = {
    "x-app-id": nut_api_id,
    "x-app-key": nut_api_key
}

nut_body = {
    "query": "swim 3 kilos",
    "gender": "male",
    "weight_kg": "85.5",
    "height_cm": "179.8",
    "age": 24
}

sheety_url = "https://api.sheety.co/b522a052a88212ddc882983bd34104a6/myWorkouts/workouts"
response = requests.post(url=nut_api_url, headers=nut_header, json=nut_body)
workout = response.json()["exercises"][0]

sheety_body = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%I:%M:%S %p"),
        "exercise": workout["name"],
        "duration": workout["duration_min"],
        "calories": workout["nf_calories"]
    }
}
# sheety_auth = {
#     "Authorization": os.environ.get("sheety_key")
# }

# response = requests.post(url= sheety_url, json= sheety_body, headers=sheety_auth)
print(response.text)
