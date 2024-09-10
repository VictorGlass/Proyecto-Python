'''
Dia 7 - Conversion de Temperatura.

1. Escribe un programa para convertir la temperatura de Celsius a Fahrenheit. 2. 
Escribe un programa para convertir la temperatura de Fahrenheit a Celsius
'''

#SOLUCION:

#Solicitud al usuario.
celsius = float(input("Ingrese la temperatura en Celsius: "))

#Convertimos celcius a farenheit utilizando la formula: (Celsius * 9/5) + 32
farenheit = (celsius * 9/5) + 32

#Imprimir el resultado
print(f"{celsius} grados Celsius son {farenheit:.2f} grados Farenheit")