from urllib import response
from fastapi import FastAPI, Path
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from thirdfriday import *
import os
import requests

load_dotenv()
app = FastAPI()

ac_phone_number = os.getenv("AC_PHONE_NUMBER")
ac_api_key = os.getenv("AC_API_KEY")
am_phone_number = os.getenv("AM_PHONE_NUMBER")
am_api_key = os.getenv("AM_API_KEY")
ms_phone_number = os.getenv("MS_PHONE_NUMBER")
ms_api_key = os.getenv("MS_API_KEY")

people_to_message = {
    ac_phone_number: ac_api_key,
    am_phone_number: am_api_key,
    ms_phone_number: ms_api_key,
}


def send_message(phone_number, api_key):
    message = f"Hello World"

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Sent message to {phone_number}")
    else:
        print(
            f"Failed to send message to {phone_number}. Status code: {response.status_code}"
        )


for person in people_to_message:
    send_message(person, people_to_message[person])
# send_message(ac_phone_number, ac_api_key)


@app.get("/")
def index():
    return (
        {"today is": today()},
        {"tomorrow is": tomorrow()},
    )
