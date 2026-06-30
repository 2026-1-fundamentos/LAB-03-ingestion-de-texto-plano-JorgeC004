"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

import pandas as pd
import re


def pregunta_01():

    path = "files/input/clusters_report.txt"

    clusters = []

    with open(path, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()


    registro = None


    for linea in lineas:

        inicio = re.match(
            r"\s*(\d+)\s+(\d+)\s+([\d,]+)\s+%\s+(.*)",
            linea
        )


        if inicio:

            if registro:
                clusters.append(registro)


            registro = {
                "cluster": int(inicio.group(1)),
                "cantidad de palabras clave": int(inicio.group(2)),
                "porcentaje de palabras clave": float(
                    inicio.group(3).replace(",", ".")
                ),
                "principales palabras clave": inicio.group(4).strip()
            }


        else:

            if registro:

                texto = linea.strip()

                if texto and not texto.startswith("-"):
                    registro["principales palabras clave"] += " " + texto



    if registro:
        clusters.append(registro)



    df = pd.DataFrame(clusters)


    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )


    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)
        .str.replace(" ,", ",")
        .str.rstrip(".")
        .str.strip()
    )


    return df