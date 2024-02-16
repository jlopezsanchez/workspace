VOCALES = 'aeiou'
frase = 'Supercalifragilisticoespialidoso'

num_vocales = 0
for letra in frase.lower():
    if letra in VOCALES:
        num_vocales += 1

print(num_vocales)
