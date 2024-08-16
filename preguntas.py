"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
        Retorne la suma de la segunda columna.

        Rta/
        214

        """
    with open("data.csv", "r") as archivo:
        suma = 0
        for linea in archivo.readlines():
            suma += int(linea.split(",")[1])
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
    with open("data.csv", "r") as archivo:
        registros = [linea.split(",")[0] for linea in archivo.readlines()]
        contador = {}
        for letra in registros:
            if letra not in contador:
                contador[letra] = 0
            contador[letra] += 1
        return sorted([(letra, cantidad) for letra, cantidad in contador.items()], key=lambda x: x[0])


def pregunta_03():
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
    with open("data.csv", "r") as archivo:
        registros = [linea.split(",")[0] for linea in archivo.readlines()]
        contador = {}
        for letra in registros:
            if letra not in contador:
                contador[letra] = 0
            contador[letra] += int(linea.split(",")[1])
        return sorted([(letra, suma) for letra, suma in contador.items()], key=lambda x: x[0])

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
    with open("data.csv", "r") as archivo:
        registros = [linea.split(",")[2].split("-")[1] for linea in archivo.readlines()]
        contador = {}
        for mes in registros:
            if mes not in contador:
                contador[mes] = 0
            contador[mes] += 1
        return sorted([(mes, cantidad) for mes, cantidad in contador.items()], key=lambda x: x[0])




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
    with open("data.csv", "r") as archivo:
        registros = [linea.split(",") for linea in archivo.readlines()]
        contador = {}
        for registro in registros:
            letra = registro[0]
            valor = int(registro[1])
            if letra not in contador:
                contador[letra] = [valor, valor]
            else:
                contador[letra][0] = max(contador[letra][0], valor)
                contador[letra][1] = min(contador[letra][1], valor)
        return [(letra, contador[letra][0], contador[letra][1]) for letra in contador]


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
    with open("data.csv", "r") as archivo:
        registros = [linea.split(",")[4].strip() for linea in archivo.readlines()]
        diccionario = {}
        for registro in registros:
            clave, valor = registro.split(":")
            if clave not in diccionario:
                diccionario[clave] = [int(valor), int(valor)]
            else:
                diccionario[clave][0] = max(diccionario[clave][0], int(valor))
                diccionario[clave][1] = min(diccionario[clave][1], int(valor))
        return [(clave, diccionario[clave][1], diccionario[clave][0]) for clave in diccionario]



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

    with open("data.csv", "r") as archivo:
        lista_registros = [(linea.split("\t")[1], linea.split("\t")[0]) for linea in archivo.readlines()]

        numeros = sorted(set(tupla[0] for tupla in lista_registros))

        lista_definitiva = []
        for numero in numeros:
            lista_filtrada = list(map(lambda x: x[1], list(filter(lambda tupla: tupla[0] == numero, lista_registros))))
            lista_definitiva.append((int(numero), lista_filtrada))

        return lista_definitiva





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
    with open("data.csv", "r") as archivo:
        lista_registros = [(linea.split("\t")[1], linea.split("\t")[0]) for linea in archivo.readlines()]

        numeros = sorted(set(tupla[0] for tupla in lista_registros))

        lista_definitiva = []
        for numero in numeros:
            lista_filtrada = sorted(set(list(map(lambda x: x[1], list(filter(lambda tupla: tupla[0] == numero, lista_registros))))))

            lista_definitiva.append((int(numero), lista_filtrada))

        return lista_definitiva





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
    with open("data.csv", "r") as archivo:


        lista_registros = list(map(lambda x: x.split(","),[linea.split("\t")[4][:-1] for linea in archivo.readlines()]))
        lista_convertida = [[elemento] for sublist in lista_registros for elemento in sublist]




        diccionario = {}
        for registro in lista_convertida:
            clave, valor = registro[0].split(":")
            if clave not in diccionario:
                diccionario[clave] = 0
            diccionario[clave] += 1

        return diccionario






pregunta_09()

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
    with open("data.csv", "r") as archivo:
        return [(linea.split("\t")[0], len(linea.split("\t")[3].split(",")), len(linea.split("\t")[-1].replace("\n","").split(",")))
                for linea in archivo.readlines()]





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
    with open("data.csv", "r") as archivo:
        lista_registros = [((linea.split("\t")[3]), int(linea.split("\t")[1])) for linea in archivo.readlines()]

        lista_transformada = list(map(lambda lista: lista[0].split(",") + [lista[1]] , lista_registros))
        diccionario = {}
        for lista in lista_transformada:
            for letra in lista[:-1]:
                if letra not in diccionario:
                    diccionario[letra] = 0
                diccionario[letra] += lista[-1]
        return dict(sorted(diccionario.items()))





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
    with open('data.csv',"r") as archivo:
        lista_registros = list((linea[0], linea.split("\t")[4][:-1]) for linea in archivo.readlines())


    diccionario = {clave[0]: 0 for clave in lista_registros}

    for letra in diccionario:
        diccionario[letra] = sum(
            list(map(lambda lista_completa: sum(list(map(lambda elemento_lista: int(elemento_lista.split(":")[1]), lista_completa))),
                list(map(lambda x: x[1].split(","),
                         list(filter(lambda x: letra in x, lista_registros)))))))

    return dict(sorted(diccionario.items()))