from flask import Flask

app = Flask(**name**)

@app.route("/")
def home():
return "FUNZIONA"

if **name** == "**main**":
import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

