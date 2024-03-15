alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z']


def cesar(texto_inicial, desplazamiento, direccion_cifrado):
  texto_final = ""
  if direccion_cifrado == "decodifica":
    desplazamiento *= -1
  for letra in texto_inicial:
    posicion = alfabeto.index(letra)
    nueva_posicion = (posicion + desplazamiento) % 27
    texto_final += alfabeto[nueva_posicion]
  print(f"Este es el resultado de {direccion_cifrado}r: {texto_final}")

direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))


cesar(texto, desplazam, direccion)

