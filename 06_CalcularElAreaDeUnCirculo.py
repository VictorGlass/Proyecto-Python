'''
Dia 6 - Calcula el area de un circulo.

1. Escribe un programa que tome el radio del circulo 
   y genere el area del circulo a 2 digitos decimales.
'''

#SOLUCION:

radio = float(input("Ingresa el radio del circulo: "))

#Valor necesario pi.
pi = 3.14

#Calcular el area del circulo usando la formula: area = π * radio^2
area = pi * (radio ** 2)

#Imprimir el area del circulo redondeada a 2 decimales:
print(f"El area del circulo es: {area}")