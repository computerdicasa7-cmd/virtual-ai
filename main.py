from flask import Flask, request
import requests
import time
import threading

app = Flask(__name__)

TOKEN = "8537405775:AAESPuTNwnEAIajnz00P1W6CaDeYo-L3YFs"
CHAT_ID = "1451965962"

ultimo_risultato = ""

def controlla_virtuale():
    global ultimo_risultato
    
    while True:
        try:
            url = "https://www.snai.it/virtuali/ultimi-risultati/hgcals-5"
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            testo = r.text

            # cerca punteggi tipo 2-1, 3-0 ecc
            import re
            risultati = re.findall(r'\d-\d', testo)

            if risultati:
                risultato = risultati[0]

                if risultato != ultimo_risultato:
                    ultimo_risultato = risultato

                    gol = int(risultato[0]) + int(risultato[2])

                    if gol <= 2:
                        pronostico = "➡️ PROSSIMA: OVER 2.5"
                    else:
                        pronostico = "➡️ PROSSIMA: UNDER 2.5"

                    messaggio = f"""⚽ SNAI MITICO FOOTBALL

Ultimo risultato: {risultato}

{pronostico}
Giocare alla prossima corsa."""

                    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                                 params={"chat_id": CHAT_ID, "text": messaggio})

        except:
            pass

        time.sleep(120)

@app.route("/", methods=["GET"])
def home():
    return "BOT VIRTUAL CALCIO ATTIVO"

threading.Thread(target=controlla_virtuale).start()
