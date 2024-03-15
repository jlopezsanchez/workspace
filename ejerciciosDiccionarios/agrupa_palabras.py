'''
Ejercicio de Diccionario
Escriba un programa en Python que acepte una lista de palabras y las agrupe por su letra inicial usando un diccionario
Entrada: [ 'mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco']
Salida: {'m': ['mesa', 'móvil', 'monitor'], 'b': ['barco', 'bandeja'], 'c': ['coche', 'casa', 'carretera'], 'a': ['avión', 'arco']}
'''
# Crea una lista de palabras
palabras = [
    'mesa',
    'móvil',
    'barco',
    'coche',
    'avión',
    'bandeja',
    'casa',
    'monitor',
    'carretera',
    'arco',
]

#Define un diccionario vacio
palabras_agrupadas = {}

# Bucle que recorre la lista de palabras
for palabra in palabras:
    clave = palabra[0] # Accede a la inicial de cada palabra
    if clave in palabras_agrupadas: # Si la inicial ya existe en el diccionario, añade la palabra a los valores que ya tenia la clave
        palabras_agrupadas[clave].append(palabra)
    else: # Si no existe añade la clave y el valor
        palabras_agrupadas[clave] = [palabra]

print(palabras_agrupadas)
