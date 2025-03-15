import pytest
from dotenv import load_dotenv
import os
import requests

load_dotenv()

ac_phone_number = os.getenv("AC_PHONE_NUMBER")
ac_api_key = os.getenv("AC_API_KEY")


def test_api_status_ok():
    message = "[TEST]: Successfully sent message"

    url = f"https://api.callmebot.com/whatsapp.php?phone={ac_phone_number}&text={message}&apikey={ac_api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Sent message to {ac_phone_number}")
    else:
        print(
            f"Failed to send message to {ac_phone_number}. Status code: {response.status_code} - {response.text}"
        )
