numero = int(input("Dígame un número: "))
diccionario = {'a': 100, 'b': 200, 'c': 300} 

if numero in diccionario.values():
    print(f'El número {numero} está en el dicccionario')
else:
    print(f'El número {numero} no está en el dicccionario')