import requests

nut_api_id = "d028dcfa"
nut_api_key = "52c470f7feabb9963a54edd3f1ea6472"
nut_api_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

nut_header = {
    "x-app-id" : nut_api_id,
    "x-app-key" : nut_api_key
}

nut_body = {
    "query" : "swim 3 kilos",
    "gender" : "male",
    "weight_kg": "85.5",
    "height_cm": "179.8",
    "age": 24
}

response = requests.post(url=nut_api_url, headers=nut_header, json=nut_body)
print(response.text)