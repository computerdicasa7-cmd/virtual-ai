import requests
import time
from flask import Flask
import threading

TOKEN = "8537405775:AAESPuTNwnEAIajnz00P1W6CaDeYo-L3YFs"
CHAT_ID = "1451965962"

app = Flask(name)

def manda_messaggio(testo):
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": testo}
try:
requests.post(url, data=data, timeout=10)
except:
pass

def controlla_risultati():
ultimo = ""

```
while True:
    try:
        r = requests.get("https://virtual-proxy.snai.it/virtual/results/hgcals-5", timeout=15)
        dati = r.json()

        partita = dati["lastEvent"]["score"]

        if partita != ultimo:
            ultimo = partita
            manda_messaggio("⚽ Nuovo risultato virtuale: " + partita)

    except Exception as e:
        print("errore:", e)

    time.sleep(20)
```

@app.route('/')
def home():
return "Bot virtuali attivo"

def avvia_bot():
t = threading.Thread(target=controlla_risultati)
t.start()

avvia_bot()
