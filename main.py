from fastapi import FastAPI  
from fastapi.responses import HTMLResponse  
from datetime import datetime  
import random  

app = FastAPI()  

@app.get("/", response_class=HTMLResponse)  
def home():  

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
    </head>  
    <body style="background:#0f172a;color:white;text-align:center;font-family:Arial;margin-top:100px;">  
        <h1>PRONOSTICO LIVE</h1>  
        <h2>{pick}</h2>  
        <p>Probabilità: {conf}%</p>  
        <p>Aggiornato: {now}</p>  
    </body>  
    </html>  
    """  
