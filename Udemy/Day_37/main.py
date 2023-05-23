import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": "1298gr9()9Yjhoefw@",
    "username": "harigaze",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
# response = requests.post(url= pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{params['username']}/graphs"
graph_config = {
    "id": "graph1",
    "name": "coding graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": params["token"]
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(response.text)
today = datetime(year=2023, month=5, day=22)
pixel_post = f"{pixela_endpoint}/{params['username']}/graphs/{graph_config['id']}"
pixel_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2"
}

# response = requests.post(url= pixel_post, json= pixel_body, headers= headers)
# print(response.text)
response = requests.put(url=f"{pixel_post}/{today.strftime('%Y%m%d')}", json={"quantity": "1"}, headers=headers)
print(response.text)
