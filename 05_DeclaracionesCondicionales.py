'''
Dia 5 - Declaraciones Condicionales.

1. Escriba un programa que lea un numero entero como entrada del usuario e imprima si el numero es par o impar en la consola.
2. Escriba un programa que tome 3 numeros como entrada e imprima el mas grande de ellos.
3. Escriba un programa que comprueba si un año de entrada determinado es bisiesto o no.
4. Escriba un programa que lea el porcentaje y luego imprima su calificacion de letra correspondiente (A, B, C, D o F).
'''

#SOLUCION:

#1.

print("Bienvenido, voy a adivinar si el numero que ingresas es par o impar!")
numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print(f"Ingresaste un: {numero} y es par!")
else:
    print(f"Ingresaste un: {numero} y es impar!")



#2.
print("Bienvenido, voy a adivinar cual es el numero mas grande de los que vayas a ingresar!")
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"El primer numero ingresado fue: {num1}, y es el mayor")
elif num2 > num1 and num2 > num3:
    print(f"El segundo numero ingresado fue: {num2}, y es el mayor")
elif num3 > num1 and num3 > num2:
    print(f"El tercer numero ingresado fue: {num3}, y es el mayor")
else:
    print("Ingresa un numero entero valido!")



#3.
print("Bienvenido, ingresa un año y te dire si es año bisiesto o no")
año = int(input("Ingrese un año: "))

#Un año es bisiesto cuando es divisible por 4, pero no por 100
#a menos que tambien sea divisible por 400.
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año ingresado fue: {año}, y es bisiesto!")
else:
    print(f"El año ingresado fue: {año}, y no es bisiesto!")


#4.
print("Bienvenido!, con el porcentaje te dire tu nota!")
porcentaje = float(input("Ingresa un porcentaje: "))

if porcentaje >= 90:
    nota = 'A'
elif porcentaje >= 80:
    nota = 'B'
elif porcentaje >= 70:
    nota = 'C'
elif porcentaje >= 60:
    nota = 'D'
else:
    nota = 'F'

print(f"El porcentaje ingresado es: {porcentaje}, y tu nota es: {nota}")
    
