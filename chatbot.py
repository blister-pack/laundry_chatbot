from fastapi import FastAPI, Path
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from thirdfriday import *
import os

load_dotenv()

app = FastAPI()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

@app.get("/")
def index():
    return (
        {"today is": today()},
        {"tomorrow is": tomorrow()},
    )
