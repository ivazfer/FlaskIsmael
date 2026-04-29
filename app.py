from flask import Flask, render_template, request, abort
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cargar_ejercicios():
    ruta = os.path.join(BASE_DIR, "data", "ejercicios.json")
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    return datos["ejercicios"]


@app.route("/")
def index():
    return render_template("index.html")


app.run("0.0.0.0", 5000, debug=True)
