def busqueda_binaria(items, item_buscado):
    indice = -1
    primero = 0
    ultimo = len(items) - 1
    encontrado = False
    
    while primero <= ultimo and encontrado == False: 
        mitad = (primero + ultimo) // 2
        if items[mitad] == item_buscado: 
            indice = mitad
            encontrado = True
        elif items[mitad] < item_buscado:
            primero = mitad + 1 # Focus on right half of range
        else:
            ultimo = mitad - 1
    return indice

posicion = busqueda_binaria([0, 1, 3, 4, 12, 23, 34, 54], 54)
print(posicion)