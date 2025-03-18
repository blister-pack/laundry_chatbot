from contextlib import asynccontextmanager
import asyncio
from fastapi import FastAPI, Path
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from dotenv import load_dotenv
from source.business_logic import *
import os
import requests
from messaging import message_start_service, message_everyone
import httpx

load_dotenv()
scheduler = AsyncIOScheduler()

APP_URL = os.getenv("APP_URL")
if not APP_URL:
    raise ValueError("APP_URL is not set in environment variables.")


async def self_ping():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{APP_URL}/ping")
            print(f"Self-ping status: {response.status_code}")
        except Exception as e:
            print(f"Self-ping failed: {str(e)}")


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
