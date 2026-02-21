from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
import requests
import os
import asyncio

app = FastAPI()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=data, timeout=10)
    except:
        pass

def generate_tip():
    value = random.random()

    if value > 0.72:
        return "🔥 VIRTUAL CALCIO: GIOCA OVER 1.5"
    elif value < 0.18:
        return "🔥 VIRTUAL CALCIO: GIOCA UNDER 2.5"
    else:
        return None

async def loop_predictions():
    while True:
        tip = generate_tip()
        if tip:
            send_telegram(tip)
        await asyncio.sleep(180)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(loop_predictions())

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Bot Virtuali attivo</h1>
    <p>Se stai leggendo questo, il sistema è collegato a Telegram.</p>
    """
