from fastapi import FastAPI, Path
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from thirdfriday import *
import os

load_dotenv()
app = FastAPI()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
my_phone_number = os.getenv("MY_PHONE_NUMBER")




@app.get("/")
def index():
    return (
        {"today is": today()},
        {"tomorrow is": tomorrow()},
    )
