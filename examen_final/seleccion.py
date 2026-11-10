def seleccion(lista):
    datos = lista.copy()
    n = len(datos)
    iteraciones = 0

    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            iteraciones += 1
            if datos[j] < datos[menor]:
                menor = j
        aux = datos[i]
        datos[i] = datos[menor]
        datos[menor] = aux

    return datos, iteraciones