import requests
from bs4 import BeautifulSoup
import time

TOKEN = "8537405775:AAESPuTNwnEAIajnz00P1W6CaDeYo-L3YFs"
CHAT_ID = "1451965962"

URL = "https://www.snai.it/virtuali/ultimi-risultati/hgcals-5"

ultimo_risultato = ""

def manda_telegram(messaggio):
requests.get(
f"https://api.telegram.org/bot{TOKEN}/sendMessage",
params={"chat_id": CHAT_ID, "text": messaggio}
)

def analizza():
global ultimo_risultato

```
r = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(r.text, "html.parser")

partite = soup.find_all("div")

for p in partite:
    testo = p.get_text()

    if "-" in testo and ":" in testo:
        if testo != ultimo_risultato:
            ultimo_risultato = testo

            # ANALISI SEMPLICE
            if "0-0" in testo or "1-0" in testo or "0-1" in testo:
                previsione = "OVER 2.5 PROBABILE"
            else:
                previsione = "UNDER 3.5 PROBABILE"

            manda_telegram(
                f"Nuovo risultato Mitico Football:\n{texto}\n\nProssima giocata consigliata:\n{previsione}"
            )
```

while True:
try:
analizza()
time.sleep(120)
except:
time.sleep(60)
