from flask import Flask
import requests
import time
import threading
import re

app = Flask(__name__)

TOKEN = "8537405775:AAESPuTNwnEAIajnz00P1W6CaDeYo-L3YFs"
CHAT_ID = "1451965962"

ultimo_risultato = None
def controlla_virtuale():
    global ultimo_risultato
    
    while True:
        try:
            api = "https://www.snai.it/scommesse/virtuali/hub/last-results/hgcals-5"
            r = requests.get(api, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
            data = r.json()

            partite = data["lastResults"]

            if partite:
                partita = partite[0]
                casa = partita["homeTeamName"]
                ospite = partita["awayTeamName"]
                gol_casa = partita["homeScore"]
                gol_ospite = partita["awayScore"]

                risultato = f"{gol_casa}-{gol_ospite}"

                if risultato != ultimo_risultato:
                    ultimo_risultato = risultato

                    totale = gol_casa + gol_ospite

                    if totale <= 2:
                        pronostico = "➡️ PROSSIMA: OVER 2.5"
                    else:
                        pronostico = "➡️ PROSSIMA: UNDER 2.5"

                    messaggio = f"""⚽ SNAI MITICO FOOTBALL

{casa} vs {ospite}
Risultato: {risultato}

{pronostico}
Gioca sulla prossima corsa."""

                    requests.get(
                        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                        params={"chat_id": CHAT_ID, "text": messaggio}
                    )

        except Exception as e:
            print("errore:", e)

        time.sleep(90)

@app.route("/")
def home():
    return "BOT VIRTUAL CALCIO ATTIVO"


def avvia_bot():
    t = threading.Thread(target=controlla_virtuale)
    t.daemon = True
    t.start()

avvia_bot()
