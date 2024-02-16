edad = int(input("Introduce tu edad: "))
peso = int(input("Introduce tu peso: "))
pulso = int(input("Introduce tu pulso: "))
plaquetas = int(input("Introduce tus plaquetas: "))

''' Condiciones para poder donar sangre:
   * 18 años < edad < 65 años
   * peso > 55 kg
   * 50 ppm > pulso < 110 ppm
   * plaquetas > 150000
'''
if edad > 18 and edad < 65:
    if peso > 55:
        if pulso > 50 and pulso < 110:
            if plaquetas > 150000:
                print("Usted puede donar sangre.")
            else:
                print("Usted NO puede donar sangre. No cumple los requisitos del peso")
        else:
                print("Usted NO puede donar sangre. No cumple los requisitos del pulso cardiaco")
    else:
                print("Usted NO puede donar sangre. No cumple los requisitos de las plaquetas")
else:
                print("Usted NO puede donar sangre. No cumple los requisitos de la edad")