'''
Día 8 - Calculadora Simple

Crea un programa de calculadora simple que pueda sumar, restar, multiplicar y dividir dos números enteros
'''

#SOLUCION: 

print("App Calcutator")
print("Bienvenido! Vamos a hacer unas operaciones aritmeticas")
print()

while True:
    print("Selecciona que operacion artimetica quieres realizar")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Salir")
    print()

    opcion1 = int(input("Ingresa una opcion: "))
    print()

    #Suma
    if opcion1 == 1:
        print("Vamos a sumar dos valores")
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        suma = num1 + num2
        print(f"La suma de {num1} mas {num2} da como resultado: {suma}")
        print()

    #Resta
    elif opcion1 == 2:
        print("Vamos a restar dos valores")
        num3 = int(input("Ingrese un numero: "))
        num4 = int(input("Ingresa otro numero: "))
        resta = num3 - num4
        print(f"La resta de {num3} menos {num4} da como resultado: {resta}")
        print()

    #Multiplicacion
    elif opcion1 == 3:
        print("Vamos a multiplicar dos valores")
        num5 = int(input("Ingresa un numero: "))
        num6 = int(input("Ingresa otro numero: "))
        multiplicar = num5 * num6
        print(f"La multiplicacion de {num5} por {num6} da como resultado: {multiplicar}")
        print()
    #Division
    elif opcion1 == 4:
        print("Vamos a dividir dos valores")
        num7 = int(input("Ingresa un numero: "))
        num8 = int(input("Ingresa otro numero: "))
        dividir = num7 / num8
        print(f"La division de {num7} y {num8} da como resultado: {dividir:.0f}")
        print()
    #Salir
    elif opcion1 == 5:
        print("Saliendo de la calculadora. ¿Gracias por usarla!")
        print()
        break

    else:
        print("Error! Por favor ingresa una de las 4 opciones disponibles")




    