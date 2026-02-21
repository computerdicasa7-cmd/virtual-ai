from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TOKEN = os.getenv("8537405775:AAESPuTNwnEAIajnz00P1W6CaDeYo-L3YFs")

results = []

def send(msg, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": msg})

def analyze(chat_id):
    if len(results) < 6:
        return

    last8 = results[-8:]
    goals = [int(x.split("-")[0]) + int(x.split("-")[1]) for x in last8]
    avg = sum(goals)/len(goals)

    under_streak = 0
    for g in reversed(goals):
        if g <= 1:
            under_streak += 1
        else:
            break

    high_goals_absent = all(g <= 2 for g in last8[-4:])

    if avg < 2.2 and (under_streak >= 2 or high_goals_absent):
        send("📊 SNAI MITICO FOOTBALL\nFinestra favorevole!\nGIOCA ORA: OVER 1.5 sulla prossima partita", chat_id)

@app.post("/")
async def telegram_webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text","")

        if "-" in text:
            results.append(text.strip())
            analyze(chat_id)
            send("Risultato registrato ✔️", chat_id)

    return {"ok": True}
