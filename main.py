from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from datetime import datetime

app = FastAPI()

def calc_pick():
quota_over = round(random.uniform(1.40,1.75),2)
prob_reale = 0.72
value = (prob_reale * quota_over) - 1

```
if value > 0:
    return "OVER 1.5", int(prob_reale*100)
else:
    return "NO BET", 0
```

@app.get("/", response_class=HTMLResponse)
def home():
pick, conf = calc_pick()
time = datetime.now().strftime("%H:%M:%S")

```
return f'''
<html>
<head>
<title>Virtual Live Predictor</title>
<meta http-equiv="refresh" content="180">
<style>
body{{background:#0f172a;color:white;text-align:center;font-family:Arial;margin-top:100px}}
.card{{background:#1e293b;padding:40px;border-radius:20px;display:inline-block}}
.pick{{font-size:50px;color:#22c55e}}
.conf{{font-size:25px}}
</style>
</head>
<body>
<div class="card">
<h1>PRONOSTICO LIVE</h1>
<div class="pick">{pick}</div>
<div class="conf">Probabilità: {conf}%</div>
<p>Aggiornato: {time}</p>
</div>
</body>
</html>
'''
```
