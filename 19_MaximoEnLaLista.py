'''
Dia 19 - Máximo en la lista..

1. Escribe una funcion para encontrar el elemento maximo de una lista.
'''

#SOLUCION:

lista_maximo = [20, 15, 33, 100, 5500]

def maximo_lista(lista):
    #Usamos la funcion max(), arrojara el numero mayor dentro de la lista.
    return max(lista)

#Creamos una variable que almacenara los valores y dara el resultado.
resultado = maximo_lista(lista_maximo)
print(f"Los valores de la lista son los siguientes: {lista_maximo}, y el numero mayor dentro de la lista es: {resultado}")