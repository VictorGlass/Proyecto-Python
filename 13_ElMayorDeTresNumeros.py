'''
Dia 13 - El mayor de tres numeros.

1. Escribe un programa para encontrar el mayor de tres numeros 
'''

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

while True:
    if num1 > num2 and num1 > num3:
        print(f"El primer numero fue: {num1} y es el mayor de los tres numeros ingresados")
    elif num2 > num1 and num2 > num3:
        print(f"El segundo numero ingresado fue: {num2} y es el mayor de los tres numeros ingresados")
    elif num3 > num1 and num3 > num2:
        print(f"El tercer numero ingresado fue: {num3} y es el mayor de los tres numeros ingresados")
    else:
        print("Ninguno es el mayor, todos son iguales")
    break