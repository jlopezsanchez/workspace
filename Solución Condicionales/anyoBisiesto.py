anyo = 2020

divpor4 = (anyo % 4 == 0) and (anyo % 100 != 0)
divpor400 = anyo % 400 == 0

if divpor4 or divpor400:
    print('¡Año bisiesto!')
else:
    print('Año no bisiesto')
