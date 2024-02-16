eleccion1 = 'piedra'
eleccion2 = 'papel'

if eleccion1 == eleccion2:
    mensaje = 'Empate'
    ganador = 0
elif eleccion1 == 'piedra' and eleccion2 == 'tijera':
    mensaje = 'La piedra aplasta la tijera'
    ganador = 1
elif eleccion1 == 'tijera' and eleccion2 == 'piedra':
    mensaje = 'La piedra aplasta la tijera'
    ganador = 2
elif eleccion1 == 'tijera' and eleccion2 == 'papel':
    mensaje = 'La tijera corta el papel'
    ganador = 1
elif eleccion1 == 'papel' and eleccion2 == 'tijera':
    mensaje = 'La tijera corta el papel'
    ganador = 2
elif eleccion1 == 'papel' and eleccion2 == 'piedra':
    mensaje = 'El papel envuelve la piedra'
    ganador = 1
elif eleccion1 == 'piedra' and eleccion2 == 'papel':
    mensaje = 'El papel envuelve la piedra'
    ganador = 2

if ganador == 0:
    mensaje = 'Empate'
else:
    mensaje = f'Gana persona{ganador}: {mensaje}'

print(mensaje)
