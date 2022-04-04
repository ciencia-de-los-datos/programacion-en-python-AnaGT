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
    tabla = [[row[0]]+ [int(row[1])]+ row[2:] for row in tabla]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    for num in tabla:
        suma += (num[1])
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
    lisletras=[]
    lisfinal= []
    for a in tabla:
        lisletras.append(a[0])
    for b in set(lisletras):
        counter= 0
        for lista in tabla:
            if lista[0]==b:
                counter=counter+lista[1]
        lisfinal.append((b,counter))
    return sorted(lisfinal)
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
    lisletras= []
    lisfinal= []
    for a in tabla:
        lisletras.append(a[0])
    for letra in set(lisletras):
        maximo= max([z[1]for z in tabla if z[0]==letra[0]])
        minimo= min([z[1]for z in tabla if z[0]==letra[0]])
        lisfinal.append((letra,maximo,minimo))
    return sorted(lisfinal)


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
    val0= [z[0] for z in tabla if z[1]==0]
    val1= [z[0] for z in tabla if z[1]==1]
    val2= [z[0] for z in tabla if z[1]==2]
    val3= [z[0] for z in tabla if z[1]==3]
    val4= [z[0] for z in tabla if z[1]==4]
    val5= [z[0] for z in tabla if z[1]==5]
    val6= [z[0] for z in tabla if z[1]==6]
    val7= [z[0] for z in tabla if z[1]==7]
    val8= [z[0] for z in tabla if z[1]==8]
    val9= [z[0] for z in tabla if z[1]==9]
    resultado = [(0, val0), (1,val1),(2, val2), (3,val3),(4,val4), (5, val5), (6,val6),(7, val7), (8,val8),(9,val9)]
    return resultado
    


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
    val0= set([z[0] for z in tabla if z[1]== 0])
    val1= set([z[0] for z in tabla if z[1]== 1])
    val2= set([z[0] for z in tabla if z[1]== 2])
    val3= set([z[0] for z in tabla if z[1]== 3])
    val4= set([z[0] for z in tabla if z[1]== 4])
    val5= set([z[0] for z in tabla if z[1]== 5])
    val6= set([z[0] for z in tabla if z[1]== 6])
    val7= set([z[0] for z in tabla if z[1]== 7])
    val8= set([z[0] for z in tabla if z[1]== 8])
    val9= set([z[0] for z in tabla if z[1]== 9])
    resultado = [(0, list(sorted(val0))),(1,list(sorted(val1))),(2,list(sorted(val2))), (3,list(sorted(val3))),(4,list(sorted(val4))), (5, list(sorted(val5))), (6,list(sorted(val6))),(7, list(sorted(sorted(val7)))),(8,list(sorted(val8))),(9,list(sorted(val9)))]
    return resultado


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
