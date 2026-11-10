import random


def crear_lista():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 100))
    return lista