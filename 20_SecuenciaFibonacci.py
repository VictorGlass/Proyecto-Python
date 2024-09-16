'''
Dia 20 - Secuencia Fibonacci.

1. Escribe una funcion para calcular la secuencia de Fibonacci hasta cierto limite.
'''

#SOLUCION:

#Funcion con parametro limite.
def secuencia_fibonacci(limite):

    #Lista para almacenar la secuencia.
    fibonacci = []

    #Variables parta los primeros dos valores de la secuencia.
    a, b = 0, 1

    #Bucle
    while a <= limite:
        fibonacci.append(a)
        #Actualizar los valore de a y b
        a, b = b, a + b
    return fibonacci

limite = 100
resultado = secuencia_fibonacci(limite)
print(f"Secuencia de Fibonacci hasta {limite} : {resultado}")
