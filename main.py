import smtplib
import datetime as dt
import random

MY_EMAIL = "app@gmail.com"
MY_PASSWORD = "abcd1234"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1: # day number of week
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n"
                                f"{quote}")








# import smtplib
#
# my_email = "appinfo779@gmail.com"
# password = "gdhu756"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Hello")
# connection.close()


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
#
# date_of_birthday = dt.datetime(year=1991, month=11, day=6)
# print(date_of_birthday)


