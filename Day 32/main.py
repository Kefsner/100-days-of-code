import smtplib
import pandas as pd
import datetime as dt
import random

MY_EMAIL = "kesleypython@gmail.com"
PASSWORD = "k y q c h b n u e u d u l h j x"
now = dt.datetime.now()


def send_email(name, year, email):
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
        message = letter.read().replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:It is your {now.year - year} birthday!\n\n{message}"
        )


with open("birthdays.csv") as birthdays_csv:
    birthdays_dict = pd.read_csv(birthdays_csv, index_col=0).to_dict()
for key in birthdays_dict["month"]:
    if birthdays_dict["month"][key] == now.month:
        if birthdays_dict["day"][key] == now.day:
            send_email(name=key, year=birthdays_dict["year"][key], email=birthdays_dict["email"][key])
