
from source.business_logic import *
import os
import requests
from dotenv import load_dotenv

load_dotenv()

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

messages_to_send = {
    "monday": "This friday no laundry should be left hanging! Consider drying your clothes today and not later in the week!",
    "tuesday": "Getting close to Friday! Maybe you can still put some clothes to dry.",
    "wednesday": "It's already Wednesday, consider not washing any clothes today.",
    "thursday": "Tomorrow is Friday! Did you leave any clothes downstairs?",
    "friday": "Today is the day! Get your clothes from downstairs if you haven't already!",
}

all_third_fridays = get_all_third_fridays()


def send_message(phone_number, api_key):
    message = messages_to_send[today()]

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Sent message to {phone_number}")
    else:
        print(
            f"Failed to send message to {phone_number}. Status code: {response.status_code}"
        )


def message_start_service(phone_number=ac_phone_number, api_key=ac_api_key):
    message = "Scheduler started! Messages will be sent when the time is right :)"

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Sent message to {phone_number}")
    else:
        print(
            f"Failed to send message to {phone_number}. Status code: {response.status_code} - {response.text}"
        )


def message_everyone():
    """the function is ran every day, first it checks if
    it's the right week to send messages, if it is then
    the messages are sent to all members"""
    if is_right_week():
        for person in people_to_message:
            send_message(person, people_to_message[person])



def message_dev(phone_number=ac_phone_number, api_key=ac_api_key):
    message = "This message is sent every minute"

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Sent message to {phone_number}")
    else:
        print(
            f"Failed to send message to {phone_number}. Status code: {response.status_code} - {response.text}"
        )
