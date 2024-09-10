'''
Dia 15 - Factorial.

1. Escribe una funcion para calcular el factorial de un numero.
'''

#SOLUCION:

'''
La funcion para calcular el factorial de un numero debe funcionar de esta manera:

1. Entrada del numero.

2. Inicializacion: Inicializamos una variable 'resultado' en 1.
   Esta variable almacenara el valor del factorial.

3. Bucle for: El bucle for va desde 1 hasta 'numero', multiplicando cada numero por el valor acumulado en 'resultado'.

4. Resultado: Ya cuando el bucle termina, devolvera el valor de 'resultado', que contiene el facorial 'numero'.
'''

def factorial_numero(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i  # Cambié el 1 por i
    return resultado

numero = int(input("Ingresa un número: "))
print(f"El factorial de {numero} es: {factorial_numero(numero)}")
