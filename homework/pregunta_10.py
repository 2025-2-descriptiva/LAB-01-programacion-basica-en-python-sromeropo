"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultado = []
    with open("c:/GitHub/Descriptiva/LAB-01-programacion-basica-en-python-sromeropo/files/input/data.csv", "r") as file:
        for line in file:
            campos = line.strip().split("\t")
            letra = campos[0]
            num_col4 = len(campos[3].split(","))
            num_col5 = len(campos[4].split(","))
            resultado.append((letra, num_col4, num_col5))
    return resultado
