"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("c:/GitHub/Descriptiva/LAB-01-programacion-basica-en-python-sromeropo/files/input/data.csv", "r") as file:
        total = 0
        for line in file:
            total += int(line.split("\t")[1])
    return total

