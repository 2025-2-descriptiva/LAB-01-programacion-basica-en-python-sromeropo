"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_col5 = {}
    with open("../files/input/data.csv", "r") as file:
        for line in file:
            campos = line.strip().split("\t")
            letra = campos[0]
            diccionario = campos[4].split(",")
            suma_valores = sum(int(item.split(":")[1]) for item in diccionario)
            if letra not in suma_col5:
                suma_col5[letra] = suma_valores
            else:
                suma_col5[letra] += suma_valores
    return dict(sorted(suma_col5.items()))
