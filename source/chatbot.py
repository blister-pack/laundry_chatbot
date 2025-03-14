from contextlib import asynccontextmanager
from urllib import response
from fastapi import FastAPI, Path
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from dotenv import load_dotenv
from source.business_logic import *
import os
import requests
from messaging import message_start_service, message_everyone

load_dotenv()
scheduler = BackgroundScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):

    message_start_service()

    scheduler.add_job(
        func=message_everyone,
        trigger=CronTrigger(hour=8, minute=0),
        id="laundry_reminder",
        name="Remind everyone about laundry",
        replace_existing=True,
    )

    scheduler.add_job(
        func=self_ping,
        trigger=IntervalTrigger(minutes=5),
        id="self_ping",
        name="Keeps app awake in Render's free tier",
        replace_existing=True,
    )

    scheduler.start()

    yield

    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)

# this is here to keep the app running on render's free tier
@app.get("/ping")
async def ping():
    return {"status": "alive", "message": "Chatbot is running"}


def self_ping():
    try:
        response = requests.get(f"{os.getenv('APP_URL')}/ping")
        print(f"Self-ping status: {response.status_code}")
    except Exception as e:
        print(f"Self-ping failed: {str(e)}")
