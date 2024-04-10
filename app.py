from flask import Flask, request, render_template
from funciones import carga_csv, peliculas_mas_recientes
import os

archivo_cartelera = 'cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)


@app.route("/")
def index():
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template(
        "index.html", lista=lista_peliculas
    )


@app.route("/generos")
def generos():
    return render_template(
        "generos.html"
    )


@app.route("/alfabetico")
def alfabetico():
    return render_template(
        "alfabetico.html"
    )


@app.route("/anio")
def anio():
    return render_template(
        "anio.html"
    )


@app.route("/pelicula/<id>")
def pelicula(id:str):
    if id in diccionario_peliculas:

    return render_template(
        "pelicula.html"
    )


if __name__ == '__main__':
    lista = carga_csv("cartelera_2024.csv")
    app.run(debug=True)