claves = ['Diez', 'Veinte', 'Treinta']
valores = [10, 20, 30]

diccionario = {}

i=0
for clave in claves:
    diccionario[clave] = valores[i]
    i+=1

print("El contenido del diccionario es: \n",diccionario)