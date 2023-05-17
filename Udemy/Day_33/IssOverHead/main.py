import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

def position_check():
    if abs(iss_latitude - MY_LAT) > 5 or abs(iss_longitude - MY_LONG) > 5:
        return False
        #raise Exception("Your position is way too far from ISS.")
    else:
        return True


parameters = {
    "position": {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    },
    "naver_account": {
        "user": "dlrkd1122",
        "password": "Harigaze1!"
    },
    "to_send": {
        "email": [
            "dlrkd1122@gmail.com",
            "dlrkd1122@naver.com"
        ]
    },
    "msg_param": {
        "From": "dlrkd1122@naver.com",
        "To": "For Who want to see the ISS.",
        "Subject": "Hey! Look up to the sky! There is ISS in your position!"
    }
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters["position"])
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def night_check():
    if sunset > time_now.hour > sunrise:
        return False
        #raise Exception("You can't see the ISS in daytime.")
    else:
        return True


def notice_iss():
    if position_check() and night_check():
        with smtplib.SMTP("smtp.naver.com", port=587) as sm:
            sm.ehlo()
            sm.starttls()
            sm.login(parameters["naver_account"]["user"], parameters["naver_account"]["password"])
            msg = MIMEText("It's time to see ISS!!")
            msg["From"] = parameters["msg_param"]["From"]
            msg["To"] = parameters["msg_param"]["To"]
            msg["Subject"] = parameters["msg_param"]["Subject"]

            for email in parameters["to_send"]["email"]:
                sm.sendmail("dlrkd1122@naver.com", email, msg.as_string())


while True:
    time_now = datetime.now()
    if time_now.second == 0:
        notice_iss()
