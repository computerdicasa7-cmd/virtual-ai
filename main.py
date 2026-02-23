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
    
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    }

    while True:
        try:
            url = "https://www.snai.it/virtuali/ultimi-risultati/hgcals-5"

            r = session.get(url, headers=headers, timeout=25)
            html = r.text

            import re
            risultati = re.findall(r'\b\d-\d\b', html)

            if risultati:
                risultato = risultati[0]

                if risultato != ultimo_risultato:
                    ultimo_risultato = risultato

                    totale = int(risultato[0]) + int(risultato[2])

                    if totale <= 2:
                        pronostico = "➡️ GIOCA OVER 2.5 ALLA PROSSIMA"
                    else:
                        pronostico = "➡️ GIOCA UNDER 2.5 ALLA PROSSIMA"

                    messaggio = f"""⚽ SNAI MITICO FOOTBALL
Ultimo risultato: {risultato}

{pronostico}"""

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
