alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z']

def codifica(texto_plano, desplazamiento):
  texto_cifrado = ""
  for letra in texto_plano:
    posicion = alfabeto.index(letra)
    nueva_posicion = (posicion + desplazamiento) % 27
    nueva_letra = alfabeto[nueva_posicion]
    texto_cifrado += nueva_letra
  print(f"El texto codificado es {texto_cifrado}")

direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))
codifica(texto, desplazam)