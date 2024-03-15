def busqueda_lineal(items, item_buscado):
    indice = -1
    actual = 0
    encontrado = False
    while actual < len(items) and not(encontrado):
        if items[actual] == item_buscado:
            indice = actual
            encontrado = True
        actual = actual + 1
    return indice

posicion = busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 23)
print(posicion)