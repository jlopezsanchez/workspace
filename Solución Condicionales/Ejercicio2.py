valorA = 7
valorB = 4
valorC = 9

if valorA < valorB:
    if valorA < valorC:
        valor_minimo = valorA
    else:
        valor_minimo = valorC
elif valorB < valorC:
    valor_minimo = valorB
else:
    valor_minimo = valorC

print(valor_minimo)
