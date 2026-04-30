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

@app.route("/ejercicios")
def ejercicios():
    lista = cargar_ejercicios()

    busqueda = request.args.get("busqueda", "")
    musculo = request.args.get("musculo", "")
    orden = request.args.get("orden", "asc")

    musculos_unicos = sorted(set(e["musculos"]["principal"]["nombre"] for e in lista))

    if busqueda:
        lista = [e for e in lista if busqueda.lower() in e["nombre"]["visible"].lower()]

    if musculo:
        lista = [e for e in lista if e["musculos"]["principal"]["nombre"] == musculo]

    lista = sorted(lista, key=lambda e: e["nombre"]["visible"], reverse=(orden == "desc"))

    return render_template(
        "ejercicios.html",
        ejercicios=lista,
        musculos=musculos_unicos,
        busqueda=busqueda,
        musculo_sel=musculo,
        orden=orden
    )


app.run("0.0.0.0", 5000, debug=True)
