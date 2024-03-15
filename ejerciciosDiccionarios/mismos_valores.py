'''
Escriba un programa en Python que acepte un diccionario y determine si todos los valores son iguales o no.
Entrada: {'Juan': 5, 'Antonio': 5, 'Inma': 5, 'Ana': 5, 'Esteban': 5}

Salida: Valores iguales
'''

diccionario_notas = {'Juan': 5, 'Antonio': 5, 'Inma': 5, 'Ana': 5, 'Esteban': 5}

notas = list(diccionario_notas.values())
primera_nota = notas[0]
for nota in notas[1:]:
    if nota != primera_nota:
        print('Valores direrentes')
        break
else:
    print('Valores iguales')
