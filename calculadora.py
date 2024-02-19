def calculadora(num1,num2,oper):
    if oper == '*':
        resultado = num1*num2
    elif oper == '/':
        resultado = num1/num2
    elif oper == '+':
        resultado = num1+num2
    elif oper == '-':
        resultado = num1-num2
    return resultado

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
operacion = input("Introduce la operación aritmética (+, -, * o /): ")
while operacion not in ('+', '-', '*', '/') :
    print("Debes de introducir una operación correcta. Vuelve a intentarlo")
    operacion = input("Introduce la operación aritmética (+, -, * o /): ")

print(f"El resultado de la operación aritmética de {numero1} {operacion} {numero2} es: {calculadora(numero1,numero2,operacion)}")