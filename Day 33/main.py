import smtplib
import requests
from datetime import datetime
import time

MY_LAT = -23.26705381
MY_LONG = -51.27737492
RANGE = 5
MY_EMAIL = "kesleypython@gmail.com"
PASSWORD = "k y q c h b n u e u d u l h j x"
MY_GMT = -3


def is_in_range():
    if MY_LAT - RANGE < float(iss_position[0]) < MY_LAT + RANGE:
        if MY_LONG - RANGE < float(iss_position[1]) < MY_LONG + RANGE:
            return True
    return False


def is_night_sky():
    return not sunrise < time_now < sunset


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS news!\n\nIt is on the sky!"
        )


# ISS DATA
response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = response.json()

iss_position = (iss_data["iss_position"]["latitude"], iss_data["iss_position"]["longitude"])

# MY LOCATION DATA

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

my_data = response.json()

sunrise = int(my_data["results"]["sunrise"].split("T")[1].split(":")[0]) + MY_GMT
sunset = int(my_data["results"]["sunset"].split("T")[1].split(":")[0]) + MY_GMT

time_now = int(str(datetime.now()).split(" ")[1].split(":")[0])

while True:
    time.sleep(60)
    if is_night_sky() and is_in_range():
        send_email()
