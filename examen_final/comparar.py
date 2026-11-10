from burbuja import burbuja
from seleccion import seleccion


def comparar(lista):
    orden_b, it_b = burbuja(lista)
    orden_s, it_s = seleccion(lista)

    print("Lista original:", lista)
    print("Burbuja:", orden_b, "- iteraciones:", it_b)
    print("Selección:", orden_s, "- iteraciones:", it_s)

    if it_b < it_s:
        print("Burbuja usó menos iteraciones")
    elif it_s < it_b:
        print("Selección usó menos iteraciones")
    else:
        print("Los dos usaron las mismas iteraciones")