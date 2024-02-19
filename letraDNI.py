letraDNI=('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q','V', 'H', 'L', 'C', 'K', 'E')
numDNI=int(input("Introduce los números de tu DNI y calcularé la letra "))
print(f"PosicionLista: {numDNI%23}")
print(f"La letra para el DNI {numDNI} es: {letraDNI[numDNI%23]}")