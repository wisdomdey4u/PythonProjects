# import os
# import smtplib
#
# my_email = os.environ["EMAIL_ADDRESS"]
# password = os.environ["EMAIL_PASSWORD"]
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=os.environ["EMAIL_RECIPIENT"],
#                         msg="Subject: Hello\n\nThis is the body of my mail.")
import datetime as dt
import random

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# microsecond = now.microsecond
#
# date_of_birth = dt.datetime(year= 1999, month= 10, day=3)
# print(date_of_birth)
import smtplib

MY_EMAIL = os.environ["EMAIL_ADDRESS"]
MY_PASSWORD = os.environ["EMAIL_PASSWORD"]

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Quote!\n\n{quote}",
        )
