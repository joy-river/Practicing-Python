import requests

question_data = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean").json()
question_data = question_data["results"]