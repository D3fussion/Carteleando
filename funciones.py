import csv
from datetime import datetime


def carga_csv(nombre_archivo: str) -> list:
    """
    Carga el archivo csv y regresa una lista
    """
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista


def peliculas_mas_recientes(lista_peliculas: list[dict]) -> list:
    """
    Regresa las peliculas de mas reciente estreno
    """
    hoy = datetime.now()
    for pelicula in lista_peliculas:
        estreno = pelicula['fecha_estreno']
        estreno = datetime.strptime(estreno, "%Y/%m/%d")
        diferencia = hoy - estreno
        pelicula['dias_desde_estreno'] = diferencia.days
    lista_peliculas.sort(key=lambda x: x['dias_desde_estreno'], reverse=False)
    lista = lista_peliculas[:5]
    return lista


if __name__ == '__main__':
    lista = carga_csv("cartelera_2024.csv")
    for i in peliculas_mas_recientes(lista):
        print("| ", end="")
        for j in i.values():
            print(f"{j} | ", end="")
        print()