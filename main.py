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
            url = "https://www.snai.it/virtuali/ultimi-risultati/hgcals-5"
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
            testo = r.text

            risultati = re.findall(r'\d-\d', testo)

            if risultati:
                risultato = risultati[0]

                if risultato != ultimo_risultato:
                    ultimo_risultato = risultato

                    gol = int(risultato[0]) + int(risultato[2])

                    if gol <= 2:
                        pronostico = "OVER 2.5"
                    else:
                        pronostico = "UNDER 2.5"

                    messaggio = f"⚽ SNAI MITICO FOOTBALL\nUltimo risultato: {risultato}\nConsiglio: {pronostico}"

                    requests.get(
                        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                        params={"chat_id": CHAT_ID, "text": messaggio}
                    )

        except Exception as e:
            print("errore:", e)

        time.sleep(120)


@app.route("/")
def home():
    return "BOT VIRTUAL CALCIO ATTIVO"


def avvia_bot():
    t = threading.Thread(target=controlla_virtuale)
    t.daemon = True
    t.start()

avvia_bot()
