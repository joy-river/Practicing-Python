# # import smtplib
# # from email.mime.text import MIMEText
# #
# # my_email = ""
# # password = ""
# #
# #
# # with smtplib.SMTP("smtp.naver.com", port=587) as connection:
# #     connection.ehlo()
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #
# #     msg = MIMEText("테스트용 메시지")
# #     msg["To"] = "dlrkd1122@naver.com"
# #     msg["Subject"] = "이메일 테스트"
# #     msg["From"] = "dlrkd1122@naver.com"
# #
# #     connection.sendmail("dlrkd1122@naver.com", "dlrkd1122@naver.com", msg.as_string())
# #
# import datetime as dt
#
# now = dt.datetime.now()
# if now.year == 2023:
#     print("wear the mask")
# print(now.weekday())
import datetime
import datetime as dt
import smtplib as sm
from email.mime.text import MIMEText
from random import choice

naver_username = ""
naver_password = ""

today = dt.datetime.now()


if today.weekday() == 1:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        with sm.SMTP("smtp.naver.com", port=587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(naver_username, naver_password)
            msg = MIMEText(choice(quotes))
            msg["From"] = "dlrkd1122@naver.com"
            msg["Subject"] = "Monday Quotes!"
            msg["Title"] = "Some Quotes"
            msg["To"] = "For Who Needs Week Starting Quetes"
            connection.sendmail("dlrkd1122@naver.com", "dlrkd1122@gmail.com", msg.as_string())
