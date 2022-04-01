"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from collections import Counter
with open("data.csv", newline="") as BD:
    datos = csv.reader(BD, delimiter="\t")
    tabla = list(datos)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    for num in tabla:
        suma += int(num[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista_letras=[z[0] for z in tabla[0:]]
    lista2 = Counter(lista_letras).most_common(5)
    
    return sorted(lista2, reverse= False)

def pregunta_03():
  diccionario = {}
  diccionario = {"A": 0, "B": 0, "C": 0,"D": 0, "E": 0}
  for row in tabla:
    sumatoria= row[1]
    if row[0]== "A":
      diccionario["A"]+= int(sumatoria)
    if row[0]== "B":
      diccionario["B"]+= int(sumatoria)
    if row[0]== "C":
      diccionario["C"]+= int(sumatoria)
    if row[0]== "D":
      diccionario["D"]+= int(sumatoria)
    if row[0]== "E":
      diccionario["E"]+= int(sumatoria)
  return list(diccionario.items()) 
"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

"""
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses = [z[2].split("-")[1] for z in tabla[0:]]
    contarmonth = Counter(meses).most_common(12)
    return sorted(contarmonth, reverse= False)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
   
   
    """
    A_max= max([z[0:2] for z in tabla if z[0]=='A'])
    A_min= min([z[0:2] for z in tabla if z[0]=='A'])
    B_max= max([z[0:2] for z in tabla if z[0]=='B'])
    B_min= min([z[0:2] for z in tabla if z[0]=='B'])
    C_max= max([z[0:2] for z in tabla if z[0]=='C'])
    C_min= min([z[0:2] for z in tabla if z[0]=='C'])
    D_max= max([z[0:2] for z in tabla if z[0]=='D'])
    D_min= min([z[0:2] for z in tabla if z[0]=='D'])
    E_max= max([z[0:2] for z in tabla if z[0]=='E'])
    E_min= min([z[0:2] for z in tabla if z[0]=='E'])
    listA=[]
    listB=[]
    listC=[]
    listD=[]
    listE=[]
    for z in tabla:
     if z[0]=='A':
       listA= A_max[0], int(A_max[1]), int(A_min[1])
     if z[0]=='A':
       listB= B_max[0],int(B_max[1]), int(B_min[1])
     if z[0]=='A':
       listC= C_max[0], int(C_max[1]), int(C_min[1])
     if z[0]=='A':
       listD= D_max[0], int(D_max[1]), int(D_min[1])
     if z[0]=='A':
       listE= E_max[0], int(E_max[1]), int(E_min[1])
       letras= [listA,listB,listC,listD,listE]
       return letras


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
