from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():

```
quota_over = round(random.uniform(1.40, 1.75), 2)
prob_reale = 0.72
value = (prob_reale * quota_over) - 1

if value > 0:
    pick = "OVER 1.5"
    conf = int(prob_reale * 100)
else:
    pick = "NO BET"
    conf = 0

now = datetime.now().strftime("%H:%M:%S")

return f"""
<html>
<head>
    <title>Virtual Live Predictor</title>
    <meta http-equiv="refresh" content="180">
    <style>
        body {{
            background:#0f172a;
            color:white;
            text-align:center;
            font-family:Arial;
            margin-top:100px;
        }}
        .card {{
            background:#1e293b;
            padding:40px;
            border-radius:20px;
            display:inline-block;
        }}
        .pick {{
            font-size:50px;
            color:#22c55e;
        }}
        .conf {{
            font-size:25px;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h1>PRONOSTICO LIVE</h1>
        <div class="pick">{pick}</div>
        <div class="conf">Probabilità: {conf}%</div>
        <p>Aggiornato: {now}</p>
    </div>
</body>
</html>
"""
```
