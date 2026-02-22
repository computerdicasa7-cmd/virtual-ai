from flask import Flask
import requests
from bs4 import BeautifulSoup
import threading
import time
import re

app = Flask(__name__)

TOKEN = "8537405775:AAESPuTNwnEAIajnz00P1W6CaDeYo-L3YFs"
CHAT_ID = "1451965962"
URL = "https://www.snai.it/virtuali/ultimi-risultati/hgcals-5"

ultimo_risultato = ""

def manda_telegram(messaggio):
try:
requests.get(
f"https://api.telegram.org/bot{TOKEN}/sendMessage",
params={"chat_id": CHAT_ID, "text": messaggio}
)
except:
pass

def analizza():
global ultimo_risultato

```
while True:
    try:
        r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")

        testo_pagina = soup.get_text()
        risultati = re.findall(r"\d-\d", testo_pagina)

        if risultati:
            ultimo = risultati[0]

            if ultimo != ultimo_risultato:
                ultimo_risultato = ultimo

                gol = int(ultimo[0]) + int(ultimo[2])

                if gol <= 2:
                    previsione = "GIOCATA: OVER 2.5"
                else:
                    previsione = "GIOCATA: UNDER 3.5"

                manda_telegram(
                    f"MITICO FOOTBALL SNAI\nUltimo risultato: {ultimo}\nConsiglio prossima corsa:\n{previsione}"
                )

        time.sleep(120)

    except:
        time.sleep(60)
```

@app.route("/")
def home():
return "BOT MITICO FOOTBALL ATTIVO"

def avvia_bot():
analizza()

threading.Thread(target=avvia_bot).start()

if __name__ == "__main__":
app.run(host="0.0.0.0", port=10000)
