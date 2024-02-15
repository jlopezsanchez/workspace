# Contar las letras en una cadena (Ejercicio 2)
nombre = input('Introduce tu nombre: ')
apellidos = input('Introduce tus apellidos: ')
nombre_apellidos=nombre+apellidos
letras_totales=len(nombre_apellidos) - nombre_apellidos.count(' ')

print("Tu nombre completo tiene " + str(letras_totales) + " carcteres.")