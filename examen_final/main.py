from lista import crear_lista
from burbuja import burbuja
from seleccion import seleccion
from comparar import comparar


def menu():
    lista = crear_lista()

    while True:
        print("\n===== MENÚ =====")
        print("1. Crear nueva lista aleatoria")
        print("2. Ordenar con burbuja")
        print("3. Ordenar con selección")
        print("4. Comparar iteraciones")
        print("5. Salir")
        print("Lista actual:", lista)

        opcion = input("Elija una opción: ")

        if opcion == "1":
            lista = crear_lista()
        elif opcion == "2":
            ordenada, it = burbuja(lista)
            print("Ordenada:", ordenada)
            print("Iteraciones:", it)
        elif opcion == "3":
            ordenada, it = seleccion(lista)
            print("Ordenada:", ordenada)
            print("Iteraciones:", it)
        elif opcion == "4":
            comparar(lista)
        elif opcion == "5":
            print("Fin del programa")
            break
        else:
            print("Opción inválida")


menu()