'''
Dia 9 - Generador de numeros aleatorios.

1. Escribe un programa que genere un numero aleatorio. 
2. Escribe un programa que genere un numero aleatorio entre 2 numeros enteros.
'''

#SOLUCION

import random
#1.
numero_aleatorio = random.randint(0, 20)
print(numero_aleatorio)

#2.
num_aleatorio = random.randint(10, 20)
print(f"Estos son los numeros aleatorios entre 10 y 20: {num_aleatorio}")

