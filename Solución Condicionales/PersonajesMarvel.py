
puedevolar = bool(input("¿Puede volar(S/N)? ") == 'S')
eshumano = bool(input("¿Es humano(S/N)? ") == 'S')
tienemascara = bool(input("¿Tiene máscara(S/N)? ") == 'S')

if puedevolar:
    if eshumano:
        if tienemascara:
            print('Ironman')
        else:
            print('Captain Marvel')
    else:
        if tienemascara:
            print('Ronan Accuser')
        else:
            print('Vision')
else:
    if eshumano:
        if tienemascara:
            print('Spiderman')
        else:
            print('Hulk')
    else:
        if tienemascara:
            print('Black Bolt')
        else:
            print('Thanos')
