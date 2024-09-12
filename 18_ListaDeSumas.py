'''
Dia 18 - Lista de Sumas.

1. Escribe una funcion para encontrar la suma de todos los elementos de una lista.
'''

#SOLUCION:

lista_sumar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sumar_lista(lista):
    #Usamos la funcion sum() para sumar todos los elementos de la lista.
    return sum(lista)

#Creamos una variable que almacenara los valores y dara el resultado.
resultado = sumar_lista(lista_sumar)
print(f"La suma de los numeros dentro de la lista es de: {resultado}")