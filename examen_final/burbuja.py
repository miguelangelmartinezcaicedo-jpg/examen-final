def burbuja(lista):
    datos = lista.copy()  # copia para no modificar la original
    n = len(datos)
    iteraciones = 0

    for i in range(n - 1):
        cambio = False
        for j in range(n - 1 - i):
            iteraciones += 1
            if datos[j] > datos[j + 1]:
                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux
                cambio = True
        if not cambio:  # si no hubo cambios ya está ordenada
            break

    return datos, iteraciones