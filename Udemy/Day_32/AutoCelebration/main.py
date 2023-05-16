##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import datetime
import os
from email.mime.text import MIMEText
from random import choice

birth_data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
today = datetime.datetime.now()
today_month = today.month
today_day = today.day
celeb = {}
templates = []
user_name = "dlrkd1122"
user_pass = "Harigaze1!"

for (root, directories, files) in os.walk("letter_templates"):
    for file in files:
        templates.append(str(open("letter_templates/" + file).read()))

with smtplib.SMTP("smtp.naver.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user_name, user_pass)
    for data in birth_data:
        if data["month"] == today_month and data["day"] == today_day:
            msg = MIMEText(choice(templates).replace("[NAME]", data["name"]))
            msg["From"] = "dlrkd1122@naver.com"
            msg["Subject"] = "Happy BirthDay!!!!"
            msg["To"] = data["name"]
            smtp.sendmail(user_name, data["email"], msg.as_string())

# python anywhere로 클라우드 실행 가능, 정해진 시간에 작동할 수 있게 할 수 있음.