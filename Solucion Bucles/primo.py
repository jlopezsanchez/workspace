n = 11

for i in range(2, n // 2):
    if n % i == 0:
        print("No es primo")
        break
else:
    print('¡Si! Es primo')
